# BRP-gewaspercelen (PDOK, meest recente jaar in de service) binnen de bbox van Hellendoorn, opgehaald per deeltegel met paginering en retries.
# Gebruik: python3 -I brp.py -> brp.json
import sys,json,time
D='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/badd7466-a102-440a-9a30-b6c10de0f032/scratchpad/hellendoorn/raw/do2/'
sys.path.insert(0,D+'tools/pylib')
import requests
from shapely.geometry import shape, box
gem=shape(json.load(open(D+'gemeente.json'))['geometry'])
minx,miny,maxx,maxy=gem.bounds
N=4; dx=(maxx-minx)/N; dy=(maxy-miny)/N
feats={}
s=requests.Session()
for i in range(N):
  for j in range(N):
    bx=(minx+i*dx,miny+j*dy,minx+(i+1)*dx,miny+(j+1)*dy)
    if not box(*bx).intersects(gem): continue
    start=0
    while True:
        for k in range(6):
            try:
                r=s.get("https://service.pdok.nl/rvo/brpgewaspercelen/wfs/v1_0",params=dict(service="WFS",version="2.0.0",request="GetFeature",typeNames="brpgewaspercelen:BrpGewas",outputFormat="application/json",srsName="EPSG:28992",bbox=f"{bx[0]},{bx[1]},{bx[2]},{bx[3]},EPSG:28992",count=1000,startIndex=start),timeout=180,headers={'User-Agent':'Mozilla/5.0'})
                j_=r.json(); break
            except Exception as e:
                print('retry',i,j,start,r.status_code if 'r' in dir() else '',str(e)[:80],flush=True); time.sleep(5)
        else:
            raise SystemExit('mislukt')
        f=j_['features']
        for x in f: feats[x.get('id') or json.dumps(x['properties'],sort_keys=True)]=x
        start+=len(f)
        if len(f)<1000: break
    print(i,j,len(feats),flush=True)
L=list(feats.values())
json.dump(L,open(D+'brp.json','w'))
print(len(L), L[0]['properties'])
