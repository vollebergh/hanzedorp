import sys,re,html,json
t=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
title=re.search(r'<title>(.*?)</title>',t,re.S); title=html.unescape(title.group(1)) if title else ''
d=re.search(r'"datePublished":"([^"]+)"',t); d=d.group(1)[:10] if d else ''
a=re.search(r'<div[^>]+class="[^"]*(?:entry-content|td-post-content|post-content|article-content)[^"]*"[^>]*>(.*)',t,re.S)
body=a.group(1) if a else t
body=re.sub(r'<(script|style)[^>]*>.*?</\1>','',body,flags=re.S)
body=re.sub(r'<(br|/p|/li|/h\d)[^>]*>','\n',body); body=re.sub(r'<[^>]+>','',body); body=html.unescape(body)
body=re.sub(r'[ \t]+',' ',body); body=re.sub(r'\n\s*\n+','\n',body).strip()
print('TITLE:',title); print('DATE:',d); print(body[:6000])
