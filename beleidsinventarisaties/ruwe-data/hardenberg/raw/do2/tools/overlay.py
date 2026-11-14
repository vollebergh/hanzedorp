import sys, json, pickle, collections
sys.path.insert(0,'/home/nick/.local/share/hanzedorp-hardenberg/raw/do2/tools/pylib')
from shapely import wkb
from shapely.geometry import shape
from shapely.ops import unary_union
D='/home/nick/.local/share/hanzedorp-hardenberg/raw/do2/'
z=int(sys.argv[1])
gem=shape(json.load(open(D+'gemeente.json'))['geometry'])
GA=gem.area/1e4
doc=json.load(open(D+'verord_doc.json'))
an=doc['annotaties']
gid2=collections.defaultdict(set)
for aid,a in an.items():
    if a.get('renvooi')=='remove': continue
    for gid in (a.get('geometry') or {}).get('ids',[]) or []:
        gid2[gid].add(f"{a['type']}|{a['name']}")
T=pickle.load(open(D+f'tiles_z{z}.pkl','rb'))
res={}
geo={}
for gid,l in T.items():
    gs=[wkb.loads(b) for b in l]
    gs=[g for g in gs if g.geom_type in ('Polygon','MultiPolygon','GeometryCollection')]
    if not gs: continue
    u=unary_union(gs).buffer(0)
    inter=u.intersection(gem)
    a=inter.area/1e4
    if a>0.01:
        res[gid]=a; geo[gid]=inter
names=collections.defaultdict(float)
for gid,a in sorted(res.items(), key=lambda kv:-kv[1]):
    n='; '.join(sorted(gid2.get(gid,{'?'})))
    print(f"{a:9.1f} ha {a/GA*100:6.1f}%  {n[:160]}  [{gid[:8]}]")
pickle.dump({'geoms':{g:geo[g].wkb for g in geo},'names':{g:sorted(gid2.get(g,[])) for g in geo}},open(D+f'overlay_z{z}.pkl','wb'))
print('gemeente ha',GA)
