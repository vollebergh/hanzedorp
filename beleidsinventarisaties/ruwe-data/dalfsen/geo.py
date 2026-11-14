import json, subprocess, urllib.parse
from shapely.geometry import shape, Point
from shapely.ops import unary_union
def get(url):
    return subprocess.run(['curl','-s','-m','120',url],capture_output=True,text=True).stdout
# gemeente boundary
u="https://service.pdok.nl/cbs/gebiedsindelingen/2024/wfs/v1_0?service=WFS&version=2.0.0&request=GetFeature&typeNames=gemeente_gegeneraliseerd&outputFormat=application/json&srsName=EPSG:28992&cql_filter="+urllib.parse.quote("statcode='GM0148'")
g=json.loads(get(u)); dalf=shape(g['features'][0]['geometry']); print('Dalfsen area km2',round(dalf.area/1e6,1), dalf.bounds)
b=dalf.bounds
bbox=f"{b[0]},{b[1]},{b[2]},{b[3]},urn:ogc:def:crs:EPSG::28992"
layers={'ONW_zone':'Informatiekaart_Natuur:IKN_Zone_Ondernemen_met_Natuur_en_Water','Natura2000':'B46_natuur_en_landschap:B4_Natura_2000-gebieden','NNN':'B46_natuur_en_landschap:B46_Natuurnetwerk_Nederland','Grondwaterbescherming':'Informatiekaart_Natuur:IKN_Grondwaterbeschermingsgebieden','Waterwingebieden':'B34_beheer_grondwater:B3_Waterwingebieden','Essen':'B46_natuur_en_landschap:B46_Essen','Landgoederen':'B73_Cultuur:B73_Landgoederen_vlakken'}
res={}
for k,l in layers.items():
    url="https://services.geodataoverijssel.nl/geoserver/ows?service=WFS&version=2.0.0&request=GetFeature&typeNames="+urllib.parse.quote(l)+"&outputFormat=application/json&srsName=EPSG:28992&bbox="+bbox
    t=get(url)
    try:
        j=json.loads(t)
    except Exception as e:
        print(k,'ERR',t[:200]); continue
    geoms=[]
    for f in j['features']:
        try: geoms.append(shape(f['geometry']))
        except: pass
    u_=unary_union(geoms) if geoms else None
    res[k]=u_
    if u_ is not None:
        inter=u_.intersection(dalf)
        print(f"{k}: {len(geoms)} features; in Dalfsen {inter.area/1e6:.1f} km2 = {100*inter.area/dalf.area:.1f}%")
        names=set()
        for f in j['features']:
            p=f['properties']; 
            for kk in ('naam','NAAM','Naam','gebiednaam','GEBIEDNAAM'):
                if kk in p: names.add(str(p[kk]))
        if names: print('   names:',sorted(names)[:12])
    else: print(k,'no features')
import pickle; pickle.dump((dalf,res),open('geo.pkl','wb'))
