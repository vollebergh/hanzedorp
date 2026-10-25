import urllib.request,urllib.parse,json
from shapely.geometry import shape
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) Chrome/130.0.0.0'}
G='geo/'
v=json.load(open(G+'voorst.json')); g=shape(v['geometry']); minx,miny,maxx,maxy=g.bounds
def wfs(base,tn,out,extra={},page=5000):
    allf=[];start=0
    while True:
        q={'service':'WFS','version':'2.0.0','request':'GetFeature','typeNames':tn,'outputFormat':'application/json','srsName':'EPSG:28992','bbox':f'{minx},{miny},{maxx},{maxy},EPSG:28992','count':page,'startIndex':start}
        q.update(extra)
        url=base+'?'+urllib.parse.urlencode(q)
        d=json.loads(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=300).read())
        fs=d['features']; allf+=fs
        if len(fs)<page: break
        start+=page
    json.dump({'type':'FeatureCollection','features':allf},open(G+out,'w'))
    print(tn,len(allf))
try: wfs('https://geoserver.gelderland.nl/geoserver/ngr_d/wfs','ngr_d:Pvbb_Stikstofemissie_beperkingengebied','stikstof.json')
except Exception as e: print('stikstof ERR',e)
try: wfs('https://service.pdok.nl/rvo/natura2000/wfs/v1_0','natura2000:Natura2000','n2000.json')
except Exception as e: print('n2000 ERR',e)
try: wfs('https://service.pdok.nl/rvo/brpgewaspercelen/wfs/v1_0','brpgewaspercelen:BrpGewas','brp.json',page=10000)
except Exception as e: print('brp ERR',e)
