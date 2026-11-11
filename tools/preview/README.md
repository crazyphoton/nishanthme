# Preview with edit overlay (local dev only)

A local preview that renders the site with drafts enabled and injects an
in-page **edit-suggestion overlay**: select text in any post, type what should
change, and it's saved to `edit-suggestions.json` for an editor/assistant to
apply.

```sh
tools/preview/run.sh
# open http://localhost:8080/
```

Requires Hugo ≥ 0.160 (the repo/CI pin is 0.163.3) and `python3`.

## How it works

- `hugo server -D` renders the site (drafts on) on an internal port (1313).
- `overlay_server.py` is a tiny proxy on port 8080 that forwards to Hugo and
  injects the overlay into HTML responses. It also exposes `/__suggest`,
  `/__suggestions`, `/__delete`, `/__clear` to store suggestions.

Select text → popup → type a fix → **Save** (or ⌘/Ctrl+Enter). Suggestions
list in the top-right panel with per-item delete and "Clear all".

## Why this never affects production

The overlay and the write-endpoints live **entirely in the Python proxy**,
which only runs when you start it locally. Production is built and deployed by
`hugo` in `.github/workflows/deploy.yml` — it never runs `overlay_server.py`,
so the deployed static site contains **no overlay and no write endpoint**.
There is also zero overlay code in any Hugo layout, partial, theme, or content
file, so `hugo` output is always clean. In short: editing is a property of the
proxy process, not of the site.

`edit-suggestions.json` and `*.log` here are local artifacts and are gitignored.
