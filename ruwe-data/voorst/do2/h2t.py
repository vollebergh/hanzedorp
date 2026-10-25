import sys,re,html
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
s=re.sub(r'<(script|style)[^>]*>.*?</\1>','',s,flags=re.S)
s=re.sub(r'</(p|div|li|h\d|tr|table|dt|dd)>',r'\n',s); s=re.sub(r'<br\s*/?>','\n',s)
s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
print(s)
