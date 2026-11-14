import sys, json, glob, os, collections
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/34361c4d-784d-4fc5-9800-df53eb03a520/scratchpad/zwartewaterland/pylib')
import mapbox_vector_tile as m
from shapely.geometry import shape, box, Polygon, MultiPolygon
from shapely.ops import unary_union
from shapely.validation import make_valid
Z=int(sys.argv[1])
s=256*3440.64/2**Z
X0,Y0=-285401.92,903401.92
gem=shape(json.load(open('zw_gemeente.json'))['geometry'])
cand=json.load(open('zw_annot_candidates.json'))
want={}  # geometry id -> names
for key,l in cand.items():
    t,n=key.split('|',1)
    if t!='gebiedsaanwijzing': continue
    for k,ids,ren in l:
        if ren=='remove': continue
        for i in ids: want.setdefault(i,set()).add(n)
polys=collections.defaultdict(list)
for f in glob.glob(f'tiles/{Z}_*.pbf'):
    _,x,y=os.path.basename(f)[:-4].split('_'); x=int(x); y=int(y)
    data=open(f,'rb').read()
    if not data: continue
    d=m.decode(data, default_options={'y_coord_down':True})
    layer=d.get('locatie')
    if not layer: continue
    ext=layer.get('extent',4096)
    ox=X0+x*s; oy=Y0-y*s
    for ft in layer['features']:
        gid=ft['properties']['geometry_id']
        if gid not in want: continue
        g=ft['geometry']
        def conv(c): return [(ox+px/ext*s, oy-py/ext*s) for px,py in c]
        def poly(rings):
            return Polygon(conv(rings[0]), [conv(r) for r in rings[1:]])
        try:
            if g['type']=='Polygon': ps=[poly(g['coordinates'])]
            elif g['type']=='MultiPolygon': ps=[poly(r) for r in g['coordinates']]
            else: continue
        except Exception as e:
            continue
        polys[gid].extend(make_valid(p) for p in ps)
res={}
ga=gem.area
for gid,pl in polys.items():
    u=unary_union(pl)
    inter=u.intersection(gem)
    a=inter.area/1e4
    if a>0.0001:
        res[gid]=(sorted(want[gid]), a, a/(ga/1e4)*100)
for gid,(n,a,p) in sorted(res.items(), key=lambda kv:-kv[1][1]):
    print(f"{a:9.1f} ha {p:6.1f}%  {'; '.join(n)}  [{gid[:8]}]")
json.dump({gid:v for gid,v in res.items()}, open(f'../overlay_result_z{Z}.json','w'))
import pickle
keep={gid:unary_union(pl).intersection(gem) for gid,pl in polys.items() if gid in res}
pickle.dump({'geoms':{g:keep[g].wkb for g in keep},'names':{g:sorted(want[g]) for g in keep}}, open(f'../overlay_geoms_z{Z}.pkl','wb'))
print('gemeente ha', ga/1e4)
