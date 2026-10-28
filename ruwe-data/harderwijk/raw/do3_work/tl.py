import json,re,sys
tp=re.compile(sys.argv[1],re.I); loc=re.compile(sys.argv[2],re.I) if len(sys.argv)>2 else None
ex=re.compile(r'brand|aangehouden|politie|overleden|verkeersongeval|ongeluk',re.I)
r=[json.loads(l) for l in open('veluwefm.jsonl')]
r.sort(key=lambda x:x['date'])
for x in r:
    if tp.search(x['title']) and not ex.search(x['title']) and (not loc or loc.search(x['title']+x['text'][:800])):
        print(x['date'][:10],x['id'],x['title'][:130])
