import json,sys
ids=set(int(i) for i in sys.argv[1:])
for l in open('veluwefm.jsonl'):
    x=json.loads(l)
    if x['id'] in ids:
        print('=====',x['id'],x['date'][:10],x['title']); print(x['link']); print(x['text'][:2500]); print()
