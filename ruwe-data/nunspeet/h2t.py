import sys,re,html
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
t=re.sub(r'(?is)<(script|style|nav|footer|header)[^>]*>.*?</\1>','',t)
t=re.sub(r'(?i)<br\s*/?>|</p>|</li>|</h\d>|</div>','\n',t)
t=re.sub(r'<[^>]+>','',t)
t=html.unescape(t)
t=re.sub(r'\n\s*\n+','\n',t)
print(t)
