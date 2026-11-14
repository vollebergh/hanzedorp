# Haalt de gemeentegrens van Hardenberg (GM0160) op.
# Primair: PDOK Kadaster Bestuurlijke gebieden WFS (laag Gemeentegebied); ter controle PDOK CBS gebiedsindelingen 2024 (gegeneraliseerd).
# Filter client-side (cql_filter wordt door PDOK genegeerd). Gebruik: python3 -I gem.py
import sys,json,os
T='/home/nick/.local/share/hanzedorp-hardenberg/raw/do2/'
sys.path.insert(0,T+'tools/pylib')
import requests
from shapely.geometry import shape
H={'User-Agent':'Mozilla/5.0'}
BB='215000,490000,275000,545000,EPSG:28992'
fn=T+'brk_gemeenten.json'
if not os.path.exists(fn):
    r=requests.get('https://service.pdok.nl/kadaster/bestuurlijkegebieden/wfs/v1_0',params=dict(service='WFS',version='2.0.0',request='GetFeature',typeNames='bestuurlijkegebieden:Gemeentegebied',outputFormat='application/json',srsName='EPSG:28992',bbox=BB,count=1000),headers=H,timeout=180)
    open(fn,'w').write(r.text)
d=json.load(open(fn))
print('BRK features',len(d['features']), d['features'][0]['properties'])
for f in d['features']:
    p=f['properties']
    if 'Hardenberg' in json.dumps(p) or '0160' in json.dumps(p):
        g=shape(f['geometry']); print('BRK',p, round(g.area/1e4,1),'ha', [round(v) for v in g.bounds])
        json.dump(f, open(T+'gemeente.json','w'))
fn2=T+'pdok_gemeenten_2024.json'
if not os.path.exists(fn2):
    r=requests.get('https://service.pdok.nl/cbs/gebiedsindelingen/2024/wfs/v1_0',params=dict(service='WFS',version='2.0.0',request='GetFeature',typeNames='gebiedsindelingen:gemeente_gegeneraliseerd',outputFormat='application/json',srsName='EPSG:28992',bbox=BB,count=1000),headers=H,timeout=180)
    open(fn2,'w').write(r.text)
for f in json.load(open(fn2))['features']:
    if f['properties'].get('statnaam')=='Hardenberg':
        print('CBS2024',f['properties'], round(shape(f['geometry']).area/1e4,1),'ha')
