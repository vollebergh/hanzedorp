import sys,json
sys.path.insert(0,'/home/nick/.local/share/hanzedorp-raalte/raw/do2/tools/pylib')
import requests
from shapely.geometry import shape
D='/home/nick/.local/share/hanzedorp-raalte/raw/do2/'
gem=shape(json.load(open(D+'raalte_gemeente.json'))['geometry'])
minx,miny,maxx,maxy=gem.bounds
feats=[];start=0
while True:
    r=requests.get("https://service.pdok.nl/rvo/brpgewaspercelen/wfs/v1_0",params=dict(service="WFS",version="2.0.0",request="GetFeature",typeNames="brpgewaspercelen:BrpGewas",outputFormat="application/json",srsName="EPSG:28992",bbox=f"{minx},{miny},{maxx},{maxy},EPSG:28992",count=1000,startIndex=start),timeout=180,headers={'User-Agent':'Mozilla/5.0'})
    j=r.json(); f=j['features']
    if not f: break
    feats+=f; start+=len(f)
    if len(f)<1000: break
json.dump(feats,open(D+'brp.json','w'))
print(len(feats), feats[0]['properties'])
