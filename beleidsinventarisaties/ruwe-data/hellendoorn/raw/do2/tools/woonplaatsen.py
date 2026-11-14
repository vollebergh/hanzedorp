# BAG-woonplaatsen binnen gemeente Hellendoorn (PDOK BAG WFS v2_0, laag woonplaats), met oppervlak en centroide.
# Gebruik: python3 -I woonplaatsen.py  -> woonplaatsen.json
import sys,json,os
T='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/badd7466-a102-440a-9a30-b6c10de0f032/scratchpad/hellendoorn/raw/do2/'
sys.path.insert(0,T+'tools/pylib')
import requests
from shapely.geometry import shape
gem=shape(json.load(open(T+'gemeente.json'))['geometry']); b=gem.bounds
fn=T+'bag_woonplaatsen.json'
if not os.path.exists(fn):
    r=requests.get('https://service.pdok.nl/lv/bag/wfs/v2_0',params=dict(service='WFS',version='2.0.0',request='GetFeature',typeNames='bag:woonplaats',outputFormat='application/json',srsName='EPSG:28992',bbox=f'{b[0]},{b[1]},{b[2]},{b[3]},EPSG:28992',count=1000),headers={'User-Agent':'Mozilla/5.0'},timeout=180)
    open(fn,'w').write(r.text)
d=json.load(open(fn)); out={}
for f in d['features']:
    g=shape(f['geometry']); g=g if g.is_valid else g.buffer(0)
    a=g.intersection(gem).area
    if a>0.5*g.area:
        p=f['properties']; c=g.centroid
        out[p.get('woonplaats') or p.get('naam')]=dict(ha=round(g.area/1e4,1),x=round(c.x),y=round(c.y),props=p)
for k,v in sorted(out.items()): print(k,v['ha'],v['x'],v['y'],v['props'].get('identificatie'),v['props'].get('status'))
print(len(out),'woonplaatsen')
json.dump(out,open(T+'woonplaatsen.json','w'),ensure_ascii=False)
