import json,sys,collections
d=json.load(open(sys.argv[1]));A=d['annotaties']
names=set(json.load(open('grid_out.json'))['verordening'][k] and n for k in [] for n in [])  # placeholder
G=json.load(open('grid_out.json'))['verordening']
present=set(n for s in G.values() for n in s)
res=collections.defaultdict(set)
def walk(n,art):
    if isinstance(n,dict):
        if n.get('type')=='artikel': art=n['kop']['nummer']['children'][0]
        for i in n.get('annotaties',[]) or []:
            a=A.get(i)
            if not a: continue
            for c in a.get('children',[]) or []:
                ca=A.get(c)
                if ca and ca.get('name') in present: res[ca['name']].add(art)
        for key in ('children','content'):
            v=n.get(key)
            if isinstance(v,list):
                for c in v: walk(c,art)
walk(d['body'][0],None)
for k in sorted(res): print(k,'->',sorted(res[k]))
