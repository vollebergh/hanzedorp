# Haalt de gemeentegrens van Raalte op (PDOK CBS gebiedsindelingen 2024; filter client-side)
import sys,json,os
T='/home/nick/.local/share/hanzedorp-raalte/raw/do2/'
sys.path.insert(0,T+'tools/pylib')
import requests
from shapely.geometry import shape
fn=T+'pdok_gemeenten_2024.json'
if not os.path.exists(fn):
    r=requests.get('https://service.pdok.nl/cbs/gebiedsindelingen/2024/wfs/v1_0',params=dict(service='WFS',version='2.0.0',request='GetFeature',typeNames='gebiedsindelingen:gemeente_gegeneraliseerd',outputFormat='application/json',srsName='EPSG:28992',bbox='190000,470000,240000,520000,EPSG:28992',count=1000),headers={'User-Agent':'Mozilla/5.0'},timeout=180)
    open(fn,'w').write(r.text)
d=json.load(open(fn))
print(len(d['features']), d['features'][0]['properties'])
for f in d['features']:
    if f['properties']['statnaam']=='Raalte':
        g=shape(f['geometry']); print(f['properties'], round(g.area/1e4,1),'ha', g.bounds)
        json.dump(f, open(T+'raalte_gemeente.json','w'))
