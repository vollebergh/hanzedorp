import pickle, json, subprocess, urllib.parse, re
from shapely.geometry import Point
from shapely.ops import unary_union
dalf,res=pickle.load(open('geo.pkl','rb'))
def geocode(q):
    u="https://api.pdok.nl/bzk/locatieserver/search/v3_1/free?rows=1&fq=type:adres&q="+urllib.parse.quote(q)
    j=json.loads(subprocess.run(['curl','-s','-m','30',u],capture_output=True,text=True).stdout)
    d=j['response']['docs'][0]; m=re.search(r'POINT\(([\d.]+) ([\d.]+)\)',d['centroide_rd']); return d['weergavenaam'],Point(float(m.group(1)),float(m.group(2)))
# Natura2000 whole-bbox is in res? need larger bbox for distance; refetch N2000 for all Overijssel
import urllib.request
n2000=subprocess.run(['curl','-s','-m','180',"https://services.geodataoverijssel.nl/geoserver/ows?service=WFS&version=2.0.0&request=GetFeature&typeNames=B46_natuur_en_landschap:B4_Natura_2000-gebieden&outputFormat=application/json&srsName=EPSG:28992&count=500"],capture_output=True,text=True).stdout
from shapely.geometry import shape
nj=json.loads(n2000); nf=[(f['properties'].get('NAAM') or f['properties'].get('naam') or str(list(f['properties'].items())[:3]), shape(f['geometry']).buffer(0)) for f in nj['features']]
print('N2000 features',len(nf))
print('N2000 in Dalfsen km2:', round(unary_union([g for _,g in nf]).intersection(dalf).area/1e6,2), '| afstand N2000 tot gemeentegrens km:', round(unary_union([g for _,g in nf]).distance(dalf)/1000,1))
pts={'De Tuindershof (Ankummer Es 11)':'Ankummer Es 11, Dalfsen','Vosserburen (Vossersteeg 74)':'Vossersteeg 74, Dalfsen','Het Engelland (Engellandweg)':'Engellandweg 1, Dalfsen','Waterinkweg Lemelerveld':'Waterinkweg 1, Lemelerveld','Oosterdalfsen Noord (Oosterdalfsersteeg)':'Oosterdalfsersteeg 1, Dalfsen','Koesteeg 19, Dalfsen':'Koesteeg 19, Dalfsen'}
for k,q in pts.items():
    try: name,p=geocode(q)
    except Exception as e: print(k,'geocode fail',e); continue
    out=[]
    for lk,g in res.items():
        d=g.distance(p)
        out.append(f"{lk.split(' ')[0]}: {'BINNEN' if d==0 else str(round(d))+' m'}")
    nn=unary_union([g for _,g in nf]).distance(p)
    print(f"{k} [{name}] RD({round(p.x)},{round(p.y)}): "+'; '.join(out)+f"; Natura2000: {round(nn)} m")
