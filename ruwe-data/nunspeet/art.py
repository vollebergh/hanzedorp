import sys,re,html
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
d=re.search(r'article:published_time" content="([^"]+)"',t) or re.search(r'datePublished"\s*:\s*"([^"]+)"',t)
ti=re.search(r'<title>(.*?)</title>',t,re.S)
print('TITLE:',html.unescape(ti.group(1).strip()) if ti else '', '| DATE:', d.group(1) if d else '?')
m=re.search(r'(?is)<div class="td-post-content[^>]*>(.*?)<div class="td-post-sharing|<div class="td-post-content[^>]*>(.*?)</article>',t)
b=(m.group(1) or m.group(2)) if m else t
b=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>','',b)
b=re.sub(r'(?i)<br\s*/?>|</p>|</li>|</h\d>','\n',b); b=re.sub(r'<[^>]+>','',b); b=html.unescape(b)
print(re.sub(r'\n\s*\n+','\n',b)[:6000])
