import sys, json, os
sys.path.insert(0,'/home/nick/.local/share/hanzedorp-raalte/raw/do2/tools/pylib')
import requests
from shapely.geometry import shape
from shapely.ops import unary_union
D='/home/nick/.local/share/hanzedorp-raalte/raw/do2/'
gem=shape(json.load(open(D+'raalte_gemeente.json'))['geometry'])
b=gem.bounds
pad=float(os.environ.get('PAD','10'))
bbox=f"{b[0]-pad},{b[1]-pad},{b[2]+pad},{b[3]+pad},urn:ogc:def:crs:EPSG::28992"
for L in sys.argv[1:]:
    fn=D+'wfs/'+L.replace(':','__')+'.json'
    if not os.path.exists(fn):
        r=requests.get('https://services.geodataoverijssel.nl/geoserver/ows',params=dict(service='WFS',version='2.0.0',request='GetFeature',typeNames=L,outputFormat='application/json',srsName='EPSG:28992',bbox=bbox),headers={'User-Agent':'Mozilla/5.0 Chrome/124'},timeout=300)
        if r.status_code!=200:
            print(L,'HTTP',r.status_code,r.text[:200]); continue
        open(fn,'w').write(r.text)
    try: d=json.load(open(fn))
    except Exception as e: print(L,'bad json',e, open(fn).read()[:300]); continue
    out=[]
    for f in d.get('features',[]):
        if not f.get('geometry'): continue
        g=shape(f['geometry'])
        if not g.is_valid: g=g.buffer(0)
        if g.intersects(gem): out.append((f['properties'],g))
    gt=out[0][1].geom_type if out else None
    if out and gt in('Polygon','MultiPolygon'):
        u=unary_union([g for _,g in out]).intersection(gem)
        a=u.area/1e4
        print(f"{L}: n={len(out)} area={a:.1f} ha = {a/(gem.area/1e4)*100:.1f}%")
    else:
        print(f"{L}: n={len(out)} type={gt} (in bbox: {len(d.get('features',[]))})")
    for p,g in out[:int(os.environ.get('SHOW','5'))]:
        print('    ',{k:v for k,v in p.items() if v not in (None,'')})
