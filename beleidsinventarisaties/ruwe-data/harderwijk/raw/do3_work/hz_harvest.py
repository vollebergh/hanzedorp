import json,re,html,urllib.request,time,sys
from hz_search import search,UA
terms=sys.argv[1:]
try: seen={json.loads(l)['url']:1 for l in open('hz.jsonl')}
except FileNotFoundError: seen={}
f=open('hz.jsonl','a')
for q in terms:
    try: r=search(q)
    except Exception as e: print(q,'ERR',e); continue
    n=0
    for h,l in r:
        if h in seen: continue
        seen[h]=1
        try: t=urllib.request.urlopen(urllib.request.Request(h,headers={'User-Agent':UA}),timeout=60).read().decode('utf-8','replace')
        except Exception as e: print('ERR',h,e); continue
        m=re.search(r'<h1[^>]*>(.*?)</h1>',t,re.S); title=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',m.group(1)))).strip() if m else ''
        d=re.search(r'(\d{1,2} (?:januari|februari|maart|april|mei|juni|juli|augustus|september|oktober|november|december) \d{4})',t)
        mm=re.search(r'<main.*?</main>',t,re.S); b=mm.group(0) if mm else t
        b=re.sub(r'<script.*?</script>|<style.*?</style>','',b,flags=re.S); b=re.sub(r'</(p|h\d|li|div)>','\n',b); b=re.sub(r'<[^>]+>','',b); b=html.unescape(b); b=re.sub(r'[ \t]+',' ',b); b=re.sub(r'\n\s*\n+','\n',b).strip()
        f.write(json.dumps({'url':h,'title':title,'date':d.group(1) if d else '','text':b,'term':q},ensure_ascii=False)+'\n'); n+=1
        time.sleep(0.4)
    print(q,len(r),'new',n,flush=True)
