import sys,re,html,urllib.parse
sys.path.insert(0,'.')
from fetch import fetch
q=sys.argv[1]; pages=int(sys.argv[2]) if len(sys.argv)>2 else 1
for pg in range(1,pages+1):
    url='https://www.vaassenactief.nl/'+('page/%d/'%pg if pg>1 else '')+'?s='+urllib.parse.quote_plus(q)
    try: d,_=fetch(url)
    except Exception as e: print('ERR',pg,e); break
    t=d.decode('utf-8','replace')
    items=re.findall(r'<h[23][^>]*class="[^"]*(?:title|entry)[^"]*"[^>]*>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',t,re.S)
    if not items: items=re.findall(r'<a[^>]+href="(https://www\.vaassenactief\.nl/[a-z0-9\-]+/)"[^>]*>([^<]{15,})</a>',t)
    seen=set()
    for h,l in items:
        if h in seen: continue
        seen.add(h); print(h,'|',html.unescape(re.sub('<[^>]+>','',l)).strip()[:110])
