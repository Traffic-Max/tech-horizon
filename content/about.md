---
title: 'HelloMotherfucker!!!'
plain: true
theme: 'dark'
---

## HelloMotherfucker!!!

{{ $style := resources.Get "css/main.css" | postCSS }}
<link href="{{ $style.RelPermalink }}" rel="stylesheet" type="text/css">

