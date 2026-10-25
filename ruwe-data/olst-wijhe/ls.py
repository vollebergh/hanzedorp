import json,sys,urllib.request
docs={'verordening':('55d637e6-8ff6-4083-a824-a0e77027a044','ov.json'),'visie':('ffe232e7-66a3-4286-a8ef-7d73d8a7d131','ovisie.json')}
pts=[l.split('|') for l in open(sys.argv[1]).read().strip().split('\n')]
for dn,(eid,fn) in docs.items():
    d=json.load(open(fn)); A=d['annotaties']
    for name,x,y in pts:
        u=f"https://ruimtelijkeplannen.overijssel.nl/api/documents/{eid}/_locationSearch?x={x}&y={y}&distance=1"
        r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})))
        names=set()
        for i in r['result']['ids']:
            a=A.get(i)
            if not a: continue
            at=a.get('attributes',{})
            extra=';'.join(f"{k}={str(v).split('/')[-1]}" for k,v in at.items() if k in('type','groep','activiteitengroep','waarde','kwalitatieveWaarde'))
            names.add(f"{a.get('type')}: {a.get('name')} [{extra}]")
        print(f"### {dn} | {name} | RD {x},{y}")
        for n in sorted(names): print('   ',n)
