import json,re,sys
pat=re.compile(sys.argv[1],re.I)
need=re.compile(sys.argv[2],re.I) if len(sys.argv)>2 else None
r=[json.loads(l) for l in open('veluwefm.jsonl')]
r.sort(key=lambda x:x['date'])
n=0
for x in r:
    s=x['title']+' '+x['text']
    if pat.search(s) and (not need or need.search(s)):
        n+=1
        print(x['date'][:10],x['id'],x['title'][:110],'|',x['link'])
print(n)
