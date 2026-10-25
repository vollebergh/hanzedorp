import json,sys,urllib.request,urllib.parse,time,os
base=sys.argv[1]; out=sys.argv[2]; terms=sys.argv[3:]
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
res={}
if os.path.exists(out): res={str(o['id']):o for o in json.load(open(out))}
for t in terms:
    for page in range(1,6):
        q=urllib.parse.urlencode({'search':t,'per_page':100,'page':page,'after':'2024-01-01T00:00:00','_fields':'id,date,link,title,content'})
        try:
            r=urllib.request.urlopen(urllib.request.Request(f'{base}/wp-json/wp/v2/posts?{q}',headers={'User-Agent':UA}),timeout=60)
            d=json.load(r)
        except Exception as e:
            break
        for o in d:
            o['terms']=sorted(set(res.get(str(o['id']),{}).get('terms',[])+[t]))
            res[str(o['id'])]=o
        if len(d)<100: break
    print(t,len(res),flush=True)
json.dump(list(res.values()),open(out,'w'),ensure_ascii=False)
