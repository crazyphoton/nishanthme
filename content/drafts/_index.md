---
title: Drafts
# The /drafts/ index itself is never built — there is no page listing them.
build:
  list: never
  render: never
# Every page in this section inherits these:
#   private: true  -> theme emits <meta name="robots" content="noindex, nofollow">
#   list: never    -> kept out of the home page, RSS feed, and sitemap.xml
#   render: always -> the page itself is still built at its own URL
cascade:
  private: true
  build:
    list: never
    render: always
---
