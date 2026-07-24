---
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
date: {{ .Date }}
draft: false
url: /drafts/{{ .File.ContentBaseName }}-{{ substr (md5 (printf "%s|%s" .File.ContentBaseName .Date)) 0 12 }}/
---
