import sys,re,html
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
ti=re.search(r'<title>(.*?)</title>',t,re.S)
d=re.search(r'(\d{1,2} \w+ 20\d\d om \d\d:\d\d)',t)
print('TITLE:',html.unescape(ti.group(1).strip()) if ti else '', '| DATE:', d.group(1) if d else '?')
i=t.find('<h1'); b=t[i:] if i>0 else t
j=b.find('Mail de redactie'); b=b[:j] if j>0 else b
b=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>','',b)
b=re.sub(r'(?i)<br\s*/?>|</p>|</li>|</h\d>','\n',b); b=re.sub(r'<[^>]+>','',b); b=html.unescape(b)
print(re.sub(r'\n\s*\n+','\n',b)[:5000])
