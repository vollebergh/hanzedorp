import json, collections
from shapely.geometry import shape, Point
from shapely.prepared import prep
G=shape(json.load(open('data/ermelo_gemeente_gm.json'))['features'][0]['geometry']); pg=prep(G)
pts=[]
for f in json.load(open('data/pdok/bag_vbo.json'))['features']:
    p=f['properties']
    if 'woonfunctie' not in (p.get('gebruiksdoel') or ''): continue
    if p['status']!='Verblijfsobject in gebruik': continue
    x,y=f['geometry']['coordinates']
    if pg.contains(Point(x,y)): pts.append((x,y,p))
print('woonobjecten in Ermelo (in gebruik, woonfunctie):',len(pts))
# grid clusters 100 m cells, connected components with radius 150 m
import math
cell=150
grid=collections.defaultdict(list)
for i,(x,y,p) in enumerate(pts): grid[(int(x//cell),int(y//cell))].append(i)
seen=set(); comps=[]
for k in grid:
    if k in seen: continue
    stack=[k]; seen.add(k); idx=[]
    while stack:
        c=stack.pop(); idx+=grid[c]
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                n=(c[0]+dx,c[1]+dy)
                if n in grid and n not in seen: seen.add(n); stack.append(n)
    comps.append(idx)
comps.sort(key=lambda c:-len(c))
out=[]
for c in comps[:25]:
    xs=[pts[i][0] for i in c]; ys=[pts[i][1] for i in c]
    streets=collections.Counter(pts[i][2]['openbare_ruimte'] for i in c).most_common(4)
    pc=collections.Counter(pts[i][2]['postcode'][:4] for i in c).most_common(2)
    print(len(c), round(sum(xs)/len(xs)), round(sum(ys)/len(ys)), pc, streets)
    out.append({'n':len(c),'x':sum(xs)/len(xs),'y':sum(ys)/len(ys),'streets':streets,'pc4':pc})
json.dump(out,open('data/woonclusters.json','w'),indent=1)
