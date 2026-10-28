import json,re,html,urllib.request,urllib.parse,time,sys
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60).read().decode('utf-8','replace')
try: seen={json.loads(l)['url'] for l in open('vrmg.jsonl')}
except FileNotFoundError: seen=set()
f=open('vrmg.jsonl','a')
for q in sys.argv[1:]:
    try: t=get('https://vrmg.nl/search?q='+urllib.parse.quote(q))
    except Exception as e: print(q,'ERR',e); continue
    m=re.search(r'<main.*?</main>',t,re.S); b=m.group(0) if m else t
    items=[]
    for h,l in re.findall(r'<a[^>]+href="(/[a-z0-9][^"/]+)"[^>]*>(.*?)</a>',b,re.S):
        l=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',l))).strip()
        if len(l)>20 and h not in [i[0] for i in items]: items.append((h,l))
    n=0
    for h,l in items:
        u='https://vrmg.nl'+h
        if u in seen: continue
        seen.add(u)
        try: a=get(u)
        except Exception as e: print('ERR',u,e); continue
        mm=re.search(r'<h1[^>]*>(.*?)</h1>',a,re.S); title=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',mm.group(1)))).strip() if mm else l[:100]
        d=re.search(r'(\d{1,2}-\d{1,2}-\d{4}|\d{1,2} (?:januari|februari|maart|april|mei|juni|juli|augustus|september|oktober|november|december) \d{4})',a)
        mm=re.search(r'<main.*?</main>',a,re.S); body=mm.group(0) if mm else a
        body=re.sub(r'<script.*?</script>|<style.*?</style>','',body,flags=re.S); body=re.sub(r'</(p|h\d|li|div)>','\n',body); body=re.sub(r'<[^>]+>','',body); body=html.unescape(body); body=re.sub(r'[ \t]+',' ',body); body=re.sub(r'\n\s*\n+','\n',body).strip()
        f.write(json.dumps({'url':u,'title':title,'date':d.group(1) if d else '','text':body,'term':q},ensure_ascii=False)+'\n'); f.flush(); n+=1
        time.sleep(0.3)
    print(q,len(items),'new',n,flush=True)
