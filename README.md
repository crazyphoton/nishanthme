# nishanth.me

This is the source for the Hugo site at `nishanth.me`.

## Writing a blog post

Each post has two Markdown files with the same name:

```text
raw-notes/posts/my-post.md     # working notes; kept in Git only
content/posts/my-post.md       # the post Hugo can publish
```

Create both files together with:

```sh
./scripts/new-post my-post
```

Write freely in `raw-notes/posts/my-post.md`, then turn the useful material
into `content/posts/my-post.md`. New posts start with `draft: true`; change it
to `draft: false` when the finished post is ready to publish.

`raw-notes/` is deliberately outside Hugo's `content/` directory. It is
version-controlled and visible on GitHub, but is not copied into the generated
website or the GitHub Pages artifact.

Repository-wide blog-writing rules for agents live in `AGENTS.md`.

An unlisted draft that needs a shareable preview can remain in
`content/posts/`, using a hard-to-guess `/drafts/.../` URL together with
`private: true` and `build.list: never`. Hugo must use `draft: false` to render
that preview; the other settings keep it out of the home page, feeds, search
engines, and sitemap.

Older shareable previews may also live in `content/drafts/`. Do not put private
or raw notes there.
