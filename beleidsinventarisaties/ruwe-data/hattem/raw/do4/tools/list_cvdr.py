import json,sys,collections
r=json.load(open(sys.argv[1]))
g=collections.defaultdict(list)
for d in r:
    base,_,v=d['identifier'].partition('_'); g[base].append(d)
rows=[]
for b,ds in g.items():
    ds.sort(key=lambda d:int(d['identifier'].split('_')[1]))
    last=ds[-1]; first=ds[0]
    rows.append((b,last.get('title'),last.get('creator'),first.get('issued'),first.get('inwerkingtredingDatum'),last.get('uitwerkingtredingDatum',''),len(ds),last.get('isRatifiedBy',''),last.get('subject','')))
rows.sort(key=lambda x:x[3] or '')
for x in rows: print(' | '.join(str(i) for i in x))
print(len(rows),'regelingen',file=sys.stderr)
print(collections.Counter(x[2] for x in rows),file=sys.stderr)
