import json,urllib.request,collections
from shapely.geometry import shape, Point
from concurrent.futures import ThreadPoolExecutor
g=shape(json.load(open('gem.json'))['features'][0]['geometry'])
print('area km2', g.area/1e6, g.bounds)
minx,miny,maxx,maxy=g.bounds; step=500
pts=[]
x=minx+step/2
while x<maxx:
    y=miny+step/2
    while y<maxy:
        if g.contains(Point(x,y)): pts.append((round(x),round(y)))
        y+=step
    x+=step
print('points',len(pts))
docs={'verordening':('55d637e6-8ff6-4083-a824-a0e77027a044','ov.json'),'visie':('ffe232e7-66a3-4286-a8ef-7d73d8a7d131','ovisie.json')}
out={}
for dn,(eid,fn) in docs.items():
    A=json.load(open(fn))['annotaties']
    def q(p):
        u=f"https://ruimtelijkeplannen.overijssel.nl/api/documents/{eid}/_locationSearch?x={p[0]}&y={p[1]}&distance=1"
        for t in range(3):
            try:
                r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60));break
            except Exception as e: r={'result':{'ids':[]}}
        s=set()
        for i in r['result']['ids']:
            a=A.get(i)
            if a and a.get('type')=='gebiedsaanwijzing' and a.get('renvooi')!='remove': s.add(a['name'])
        return p,sorted(s)
    with ThreadPoolExecutor(8) as ex: res=list(ex.map(q,pts))
    out[dn]={f"{p[0]},{p[1]}":s for p,s in res}
    c=collections.Counter(n for p,s in res for n in s)
    print('==',dn)
    for n,k in c.most_common(): print(f"  {k:4d} ({100*k/len(pts):5.1f}%) {n}")
json.dump(out,open('grid_out.json','w'))
