import sys, json, pickle, os
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/c389bf58-3dd2-4443-a542-c4ae17b8d9b4/scratchpad/deventer/tools/pylib2')
import requests, mapbox_vector_tile as mvt
from shapely.geometry import shape, box
from shapely.affinity import affine_transform
from shapely.validation import make_valid
from concurrent.futures import ThreadPoolExecutor
D='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/c389bf58-3dd2-4443-a542-c4ae17b8d9b4/scratchpad/deventer/raw2/'
VO="55d637e6-8ff6-4083-a824-a0e77027a044"
z=int(sys.argv[1])
gem=shape(json.load(open(D+'dv_gemeente.json'))['geometry'])
res=3440.64/2**z; ts=256*res
minx,miny,maxx,maxy=gem.bounds
x0=int((minx+285401.92)//ts); x1=int((maxx+285401.92)//ts)
y0=int((903401.92-maxy)//ts); y1=int((903401.92-miny)//ts)
gb=gem.buffer(50)
tiles=[(tx,ty) for tx in range(x0,x1+1) for ty in range(y0,y1+1)
       if box(-285401.92+tx*ts,903401.92-(ty+1)*ts,-285401.92+(tx+1)*ts,903401.92-ty*ts).intersects(gb)]
print(len(tiles),'tiles',flush=True)
os.makedirs(D+f'tiles/z{z}',exist_ok=True)
s=requests.Session()
def get(t):
    tx,ty=t
    fn=D+f'tiles/z{z}/{tx}_{ty}.pbf'
    if os.path.exists(fn): return t,open(fn,'rb').read()
    for k in range(5):
        try:
            r=s.get(f"https://ruimtelijkeplannen.overijssel.nl/api/documents/{VO}/tiles/{z}/{tx}/{ty}.pbf",headers={"User-Agent":"Mozilla/5.0"},timeout=90)
            if r.status_code==200:
                open(fn,'wb').write(r.content); return t,r.content
            if r.status_code in (204,404):
                open(fn,'wb').write(b''); return t,b''
        except Exception as e: pass
    return t,None
with ThreadPoolExecutor(8) as ex: out=list(ex.map(get,tiles))
print('failed',sum(1 for t,c in out if c is None),flush=True)
geoms={}; layers=set()
for (tx,ty),c in out:
    if not c: continue
    d=mvt.decode(c)
    ox=-285401.92+tx*ts; oy=903401.92-ty*ts
    for ln,l in d.items():
        layers.add(ln)
        if ln in ('label','diff'): continue
        ext=l.get('extent',4096)
        for f in l['features']:
            gid=f['properties'].get('geometry_id')
            try:
                g=shape(f['geometry'])
            except Exception: continue
            g=affine_transform(g,[ts/ext,0,0,ts/ext,ox,oy-ts])
            if not g.is_valid: g=make_valid(g)
            geoms.setdefault(gid,[]).append(g)
print('layers',layers)
pickle.dump({k:[g.wkb for g in v] for k,v in geoms.items()},open(D+f'tiles_z{z}.pkl','wb'))
print(len(geoms),'geometry ids')
