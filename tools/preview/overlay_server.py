#!/usr/bin/env python3
"""Local-only preview proxy that injects an edit-suggestion overlay.

LOCAL DEV TOOL — NOT part of the production build. The site is deployed by
`hugo` in GitHub Actions (see .github/workflows/deploy.yml), which never runs
this script. The overlay and the write-endpoint below exist ONLY while this
proxy is running locally, so they can never reach production.

Run `hugo server` (drafts on) on an internal port, then this proxy in front:

    hugo server -D --disableLiveReload --bind 127.0.0.1 --port 1313 \
        --baseURL http://localhost:8080/ --appendPort=false
    python3 tools/preview/overlay_server.py

...or just use tools/preview/run.sh. Then open http://localhost:8080/.

Routes:
  GET  *               -> forwarded to hugo; HTML gets the overlay injected.
  POST /__suggest      -> append {url, quote, comment} to edit-suggestions.json
  GET  /__suggestions  -> current suggestions as JSON
  POST /__delete       -> delete one suggestion by id
  POST /__clear        -> remove all suggestions

Config via env: PREVIEW_PORT (default 8080), HUGO_URL (default 127.0.0.1:1313).
Suggestions are written next to this script (edit-suggestions.json, gitignored).
"""
import http.server, socketserver, json, os, urllib.request, urllib.error

HUGO = os.environ.get("HUGO_URL", "http://127.0.0.1:1313")
PORT = int(os.environ.get("PREVIEW_PORT", "8080"))
SUGGESTIONS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "edit-suggestions.json")

OVERLAY = r"""
<style id="sg-style">
#sg-bar{position:fixed;top:12px;right:12px;z-index:2147483000;font:13px/1.4 -apple-system,system-ui,sans-serif;
  background:#111;color:#fff;border-radius:10px;box-shadow:0 6px 24px rgba(0,0,0,.3);width:300px;overflow:hidden}
#sg-bar h4{margin:0;padding:10px 12px;background:#1d4ed8;font-size:13px;display:flex;justify-content:space-between;align-items:center}
#sg-bar h4 span{opacity:.85;font-weight:500}
#sg-list{max-height:45vh;overflow:auto;margin:0;padding:0;list-style:none}
#sg-list:empty::after{content:"Select text in the post, then type a fix.";display:block;padding:12px;color:#aaa;font-style:italic}
#sg-list li{padding:9px 12px;border-top:1px solid #2a2a2a}
#sg-list blockquote{margin:0 0 4px;padding-left:8px;border-left:3px solid #1d4ed8;color:#bcd;font-style:italic;white-space:pre-wrap}
#sg-list .c{color:#fff;white-space:pre-wrap}
#sg-list button{float:right;background:none;border:0;color:#f87171;cursor:pointer;font-size:12px}
#sg-bar .foot{display:flex;gap:8px;padding:8px 12px;background:#161616}
#sg-bar .foot button{flex:1;background:#2a2a2a;color:#fff;border:0;border-radius:6px;padding:6px;cursor:pointer;font-size:12px}
#sg-bar .foot button:hover{background:#333}
#sg-pop{position:absolute;z-index:2147483001;background:#111;color:#fff;border-radius:8px;padding:8px;
  box-shadow:0 6px 24px rgba(0,0,0,.4);width:260px;display:none}
#sg-pop blockquote{margin:0 0 6px;padding-left:8px;border-left:3px solid #1d4ed8;color:#bcd;font-style:italic;
  font-size:12px;max-height:60px;overflow:auto;white-space:pre-wrap}
#sg-pop textarea{width:100%;box-sizing:border-box;background:#1b1b1b;color:#fff;border:1px solid #333;border-radius:6px;
  padding:6px;font:13px -apple-system,system-ui,sans-serif;resize:vertical;min-height:52px}
#sg-pop .row{display:flex;gap:6px;margin-top:6px}
#sg-pop .row button{flex:1;border:0;border-radius:6px;padding:6px;cursor:pointer;font-size:12px}
#sg-save{background:#1d4ed8;color:#fff}#sg-cancel{background:#2a2a2a;color:#fff}
.sg-hl{background:rgba(253,224,71,.45);border-radius:2px}
</style>
<div id="sg-bar">
  <h4>Edit suggestions <span id="sg-count">0</span></h4>
  <ul id="sg-list"></ul>
  <div class="foot"><button id="sg-clear">Clear all</button></div>
</div>
<div id="sg-pop">
  <blockquote id="sg-q"></blockquote>
  <textarea id="sg-t" placeholder="What should change here?"></textarea>
  <div class="row"><button id="sg-cancel">Cancel</button><button id="sg-save">Save</button></div>
</div>
<script>
(function(){
  var pop=document.getElementById('sg-pop'),qEl=document.getElementById('sg-q'),tEl=document.getElementById('sg-t'),
      listEl=document.getElementById('sg-list'),countEl=document.getElementById('sg-count');
  var pending=null;
  function esc(s){return s.replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  function render(items){
    listEl.innerHTML='';countEl.textContent=items.length;
    items.forEach(function(it){
      var li=document.createElement('li');
      li.innerHTML='<button data-id="'+it.id+'">delete</button>'+
        '<blockquote>'+esc(it.quote)+'</blockquote><div class="c">'+esc(it.comment)+'</div>';
      listEl.appendChild(li);
    });
  }
  function load(){fetch('/__suggestions').then(function(r){return r.json();}).then(render);}
  listEl.addEventListener('click',function(e){
    if(e.target.dataset.id){fetch('/__delete',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({id:e.target.dataset.id})}).then(load);}
  });
  document.getElementById('sg-clear').addEventListener('click',function(){
    if(confirm('Clear all suggestions?'))fetch('/__clear',{method:'POST'}).then(load);
  });
  document.addEventListener('mouseup',function(e){
    if(pop.contains(e.target)||document.getElementById('sg-bar').contains(e.target))return;
    var sel=window.getSelection(),txt=sel.toString().trim();
    if(txt.length<2){pop.style.display='none';return;}
    pending={quote:txt};
    qEl.textContent=txt.length>240?txt.slice(0,240)+'…':txt;
    tEl.value='';
    pop.style.left=Math.min(e.pageX,window.scrollX+window.innerWidth-280)+'px';
    pop.style.top=(e.pageY+10)+'px';pop.style.display='block';tEl.focus();
  });
  document.getElementById('sg-cancel').addEventListener('click',function(){pop.style.display='none';});
  document.getElementById('sg-save').addEventListener('click',function(){
    if(!pending)return;
    fetch('/__suggest',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({url:location.pathname,quote:pending.quote,comment:tEl.value})}).then(function(){
      pop.style.display='none';load();window.getSelection().removeAllRanges();
    });
  });
  tEl.addEventListener('keydown',function(e){if((e.metaKey||e.ctrlKey)&&e.key==='Enter')document.getElementById('sg-save').click();});
  load();
})();
</script>
"""

def read_suggestions():
    try:
        with open(SUGGESTIONS) as f: return json.load(f)
    except Exception: return []

def write_suggestions(items):
    with open(SUGGESTIONS, "w") as f: json.dump(items, f, indent=2)

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def _json(self, obj, code=200):
        body = json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}")

    def do_POST(self):
        if self.path == "/__suggest":
            d = self._body(); items = read_suggestions()
            nid = str(max([0]+[int(i["id"]) for i in items])+1)
            items.append({"id":nid,"url":d.get("url",""),"quote":d.get("quote",""),"comment":d.get("comment","")})
            write_suggestions(items); return self._json({"ok":True})
        if self.path == "/__delete":
            d = self._body(); write_suggestions([i for i in read_suggestions() if i["id"]!=d.get("id")])
            return self._json({"ok":True})
        if self.path == "/__clear":
            write_suggestions([]); return self._json({"ok":True})
        self.send_error(404)

    def do_GET(self):
        if self.path == "/__suggestions":
            return self._json(read_suggestions())
        # proxy to hugo
        try:
            req = urllib.request.Request(HUGO+self.path, headers={"Accept-Encoding":"identity"})
            with urllib.request.urlopen(req) as up:
                ctype = up.headers.get("Content-Type","")
                data = up.read()
                if "text/html" in ctype and b"</body>" in data:
                    data = data.replace(b"</body>", OVERLAY.encode()+b"</body>", 1)
                self.send_response(up.status)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(data)))
                self.end_headers(); self.wfile.write(data)
        except urllib.error.HTTPError as e:
            self.send_response(e.code); self.end_headers()
            try: self.wfile.write(e.read())
            except Exception: pass
        except Exception as e:
            self.send_error(502, str(e))

class TCP(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    if not os.path.exists(SUGGESTIONS): write_suggestions([])
    print("overlay proxy on 0.0.0.0:%d -> %s" % (PORT, HUGO))
    TCP(("0.0.0.0", PORT), Handler).serve_forever()
