# Ligging raatakkercomplexen en karrensporen(signalerings)zones t.o.v. gemeente Hardenberg, uit vector tiles z8 van de verordening-viewer (hele provincie).
import sys,json,os
T='/home/nick/.local/share/hanzedorp-hardenberg/raw/do2/'
sys.path.insert(0,T+'tools/pylib')
import requests, mapbox_vector_tile as mvt
from shapely.geometry import shape
from shapely.affinity import affine_transform
from shapely.ops import unary_union
from shapely.validation import make_valid
VO="55d637e6-8ff6-4083-a824-a0e77027a044"
d=json.load(open(T+'verord_doc.json'))
want={}
for aid,a in d['annotaties'].items():
    n=a.get('name','')
    if a.get('type')=='gebiedsaanwijzing' and ('raat' in n.lower() or 'karren' in n.lower()):
        for g in (a.get('geometry') or {}).get('ids') or []: want[g]=n
print(want)
gem=shape(json.load(open(T+'gemeente.json'))['geometry'])
z=int(sys.argv[1]) if len(sys.argv)>1 else 8
res=3440.64/2**z; ts=256*res
# provincie Overijssel ca. RD 180000-270000 x 455000-545000
x0=int((180000+285401.92)//ts); x1=int((270000+285401.92)//ts); y0=int((903401.92-545000)//ts); y1=int((903401.92-455000)//ts)
os.makedirs(T+f'tiles/z{z}',exist_ok=True)
geoms={}
for tx in range(x0,x1+1):
  for ty in range(y0,y1+1):
    fn=T+f'tiles/z{z}/{tx}_{ty}.pbf'
    if not os.path.exists(fn):
        r=requests.get(f"https://ruimtelijkeplannen.overijssel.nl/api/documents/{VO}/tiles/{z}/{tx}/{ty}.pbf",headers={"User-Agent":"Mozilla/5.0"},timeout=90)
        open(fn,'wb').write(r.content if r.status_code==200 else b'')
    c=open(fn,'rb').read()
    if not c: continue
    dd=mvt.decode(c); ox=-285401.92+tx*ts; oy=903401.92-ty*ts
    for ln,l in dd.items():
        if ln in ('label','diff'): continue
        ext=l.get('extent',4096)
        for f in l['features']:
            gid=f['properties'].get('geometry_id')
            if gid not in want: continue
            g=affine_transform(shape(f['geometry']),[ts/ext,0,0,ts/ext,ox,oy-ts])
            geoms.setdefault(gid,[]).append(make_valid(g))
for gid,l in geoms.items():
    u=unary_union(l)
    print(want[gid], gid[:8], 'opp ha',round(u.area/1e4), 'afstand tot gemeente km', round(u.distance(gem)/1000,2), 'bounds',[round(v) for v in u.bounds])
print('--- dichtstbijzijnde delen')
for gid,l in geoms.items():
    u=unary_union(l); ps=list(u.geoms) if hasattr(u,'geoms') else [u]
    for p in sorted(ps,key=lambda p:p.distance(gem))[:2]:
        c=p.representative_point(); print(want[gid], round(p.distance(gem)/1000,2),'km; punt',round(c.x),round(c.y),'opp ha',round(p.area/1e4,1))
