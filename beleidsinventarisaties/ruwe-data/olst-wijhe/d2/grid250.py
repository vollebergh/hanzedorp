import json,urllib.request,collections
from shapely.geometry import shape, Point
from concurrent.futures import ThreadPoolExecutor
g=shape(json.load(open('gem.json'))['features'][0]['geometry'])
print('area km2', round(g.area/1e6,1), [round(b) for b in g.bounds])
minx,miny,maxx,maxy=g.bounds; step=250
pts=[]
x=minx+step/2
while x<maxx:
    y=miny+step/2
    while y<maxy:
        if g.contains(Point(x,y)): pts.append((round(x),round(y)))
        y+=step
    x+=step
print('points',len(pts))
eid='55d637e6-8ff6-4083-a824-a0e77027a044'
A=json.load(open('ov_2610.json'))['annotaties']
def q(p):
    u=f"https://ruimtelijkeplannen.overijssel.nl/api/documents/{eid}/_locationSearch?x={p[0]}&y={p[1]}&distance=1"
    for t in range(4):
        try:
            r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60));break
        except Exception as e: r=None
    if r is None: return p,None
    s=set()
    for i in r['result']['ids']:
        a=A.get(i)
        if a and a.get('type')=='gebiedsaanwijzing' and a.get('renvooi')!='remove': s.add(a['name'])
    return p,sorted(s)
with ThreadPoolExecutor(10) as ex: res=list(ex.map(q,pts))
json.dump({f"{p[0]},{p[1]}":s for p,s in res},open('grid250_out.json','w'))
print('failed',sum(1 for p,s in res if s is None))
