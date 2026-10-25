import json, subprocess, urllib.parse, pickle
from shapely.geometry import shape, Point
from shapely.ops import unary_union
def get(url): return subprocess.run(['curl','-s','-m','180',url],capture_output=True,text=True).stdout
j=json.load(open('gemeenten.json'))
dalf=[shape(f['geometry']) for f in j['features'] if f['properties']['statnaam']=='Dalfsen'][0]
b=dalf.bounds; print('Dalfsen km2',round(dalf.area/1e6,1),[round(x) for x in b])
bbox=f"{b[0]},{b[1]},{b[2]},{b[3]},urn:ogc:def:crs:EPSG::28992"
layers={'ONW_zone (voormalig ONW)':'Informatiekaart_Natuur:IKN_Zone_Ondernemen_met_Natuur_en_Water','Natura2000':'B46_natuur_en_landschap:B4_Natura_2000-gebieden','NNN':'B46_natuur_en_landschap:B46_Natuurnetwerk_Nederland','Grondwaterbeschermingsgebied':'B34_beheer_grondwater:B3_Grondwaterbeschermingsgebieden','Waterwingebieden':'B34_beheer_grondwater:B3_Waterwingebieden','Essen':'B46_natuur_en_landschap:B46_Essen','Landgoederen (vlakken)':'B73_Cultuur:B73_Landgoederen_vlakken','Archeologische essen':'B73_Cultuur:B73_Archeologische_essen'}
res={}
for k,l in layers.items():
    url="https://services.geodataoverijssel.nl/geoserver/ows?service=WFS&version=2.0.0&request=GetFeature&typeNames="+urllib.parse.quote(l)+"&outputFormat=application/json&srsName=EPSG:28992&count=5000&bbox="+bbox
    t=get(url)
    try: jj=json.loads(t)
    except Exception: print(k,'ERR',t[:150]); continue
    geoms=[]
    for f in jj['features']:
        try: geoms.append(shape(f['geometry']).buffer(0))
        except Exception: pass
    if not geoms: print(f"{k}: 0 features"); continue
    u=unary_union(geoms); inter=u.intersection(dalf)
    print(f"{k}: {len(geoms)} features; binnen Dalfsen {inter.area/1e6:.1f} km2 = {100*inter.area/dalf.area:.1f}%")
    res[k]=u
pickle.dump((dalf,res),open('geo.pkl','wb'))
