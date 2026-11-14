import urllib.request,urllib.parse,json
from shapely.geometry import shape
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) Chrome/130.0.0.0'}
G='geo/'
d=json.load(open(G+'gemeente.json'))
v=[f for f in d['features'] if f['properties']['naam']=='Voorst'][0]
json.dump(v,open(G+'voorst.json','w'))
g=shape(v['geometry']); print('area ha',g.area/1e4, g.bounds)
minx,miny,maxx,maxy=g.bounds
layers=['POVE_Gelders_natuurnetwerk','POVE_Groene_ontwikkelingszone','POVE_Weidevogelgebieden','POVE_Ganzenrustgebieden','POVE_Beschzones_nat_landnat','POVE_Nationale_landschappen','POVE_Streekgebieden','POVE_Waterwingebieden','POVE_Grondwaterbescherming','POVE_Intrekgebieden','POVE_Boringsvrije_zone','POVE_Molenbiotoop','POVE_Ammoniakbuffergebied','POVE_Stiltegebieden','POVE_Oude_bosgroeiplaatsen','POVE_KWO_vrije_zone','POVE_Windturbines_aandachtsgebied_rondom_de_Veluwe','POVE_Provinciale_wegen_beperking','POVE_Neder_Germaanse_limes','POVE_Hollandse_Waterlinies','POVE_Glastuinbouw']
for L in layers:
    q={'service':'WFS','version':'2.0.0','request':'GetFeature','typeNames':'ngr_verordening:'+L,'outputFormat':'application/json','srsName':'EPSG:28992','bbox':f'{minx},{miny},{maxx},{maxy},EPSG:28992'}
    url='https://geoserver.gelderland.nl/geoserver/ngr_verordening/wfs?'+urllib.parse.urlencode(q)
    try:
        data=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=180).read()
        open(G+L+'.json','wb').write(data)
        n=len(json.loads(data)['features'])
        print(L,len(data),n)
    except Exception as e:
        print(L,'ERR',e)
