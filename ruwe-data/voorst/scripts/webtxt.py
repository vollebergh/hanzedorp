import sys,re,html,urllib.request
u=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 6000
r=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36'})
s=urllib.request.urlopen(r,timeout=60).read().decode('utf-8','replace')
m=re.search(r'<main.*?</main>',s,flags=re.S)
s=m.group(0) if m else s
s=re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>','',s,flags=re.S)
s=re.sub(r'</(p|div|li|tr|h\d)>','\n',s)
s=re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>',lambda m:m.group(2)+' ['+m.group(1)+']',s,flags=re.S)
s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s); s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
print(s[:n])
