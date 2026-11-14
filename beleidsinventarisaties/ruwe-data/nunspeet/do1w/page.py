import sys,re,html
t=open(sys.argv[1],encoding='utf8',errors='ignore').read()
m=re.search(r'<main.*?</main>',t,flags=re.S)
if m:t=m.group(0)
t=re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>','',t,flags=re.S)
t=re.sub(r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>',r'\2 [\1]',t,flags=re.S)
t=re.sub(r'<[^>]+>','\n',t);t=html.unescape(t)
t=re.sub(r'[ \t]+',' ',t);t=re.sub(r'\n\s*\n+','\n',t)
print(t)
