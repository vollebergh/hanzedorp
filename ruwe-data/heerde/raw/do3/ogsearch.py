import re,sys,html,urllib.request,urllib.parse
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=30).read().decode('utf8','ignore')
site=sys.argv[1]; q=sys.argv[2]
base={'og':'https://www.omroepgelderland.nl/zoeken?q=','oost':'https://www.rtvoost.nl/zoeken?q='}[site]
t=get(base+urllib.parse.quote(q))
t=re.sub(r'<(script|style)[^>]*>.*?</\1>','',t,flags=re.S)
seen=set()
for m in re.finditer(r'<a[^>]+href="([^"]*nieuws/[^"]+)"[^>]*>(.*?)</a>',t,flags=re.S):
    u=m.group(1); txt=html.unescape(re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',m.group(2)))).strip()
    if u in seen: continue
    seen.add(u); print(txt[:160],'|',u)
