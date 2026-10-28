# DO2 Harderwijk: clusters van agrarische grond (BRP 2025 excl. natuurterrein/overige), overlay-druk per cluster, namen via PDOK Locatieserver
import json, os, urllib.request, urllib.parse
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely import make_valid
D='data'; W=D+'/wfs'
G=shape(json.load(open(D+'/harderwijk_gemeente_gm.json'))['features'][0]['geometry'])
def L(fn):
    out=[]
    for f in json.load(open(fn))['features']:
        s=make_valid(shape(f['geometry']))
        if s.intersects(G): out.append((f['properties'],s))
    return out
def lay(fn): return make_valid(unary_union([s for p,s in L(os.path.join(W,fn))])).intersection(G)
brp=[(f['properties'],make_valid(shape(f['geometry']))) for f in json.load(open(D+'/pdok/brp2025.json'))['features']]
parts=[(p,s.intersection(G)) for p,s in brp if p['category'] not in('Natuurterrein','Overige') and s.intersects(G)]
parts=[(p,s) for p,s in parts if not s.is_empty]
OV={'GNN':lay('Gelders_natuurnetwerk.json'),'GOZ':lay('Groene_ontwikkelingszone.json'),'NatteLandnatuur':lay('Beschzones_nat_landnat.json'),
    'N-reductie':lay('Stikstofreductiegebied.json'),'Intrekgebied':lay('Intrekgebieden.json'),'Molenbiotoop':lay('Molenbiotoop.json'),'NL Veluwe':lay('Nationale_landschappen.json'),
    'Waterwin':lay('Waterwingebieden.json'),'GWBG':lay('Grondwaterbescherming.json')}
OV['N2000']=make_valid(unary_union([s for p,s in L(D+'/pdok/natura2000.json')])).intersection(G)
OV['Veluwe-streek']=make_valid(unary_union([s for p,s in L(W+'/Streekgebieden.json') if p['streekgebied_naam']=='Veluwe'])).intersection(G)
OV['Randmeerkust']=make_valid(unary_union([s for p,s in L(W+'/Streekgebieden.json') if p['streekgebied_naam']=='Randmeerkust'])).intersection(G)
agr=unary_union([s for p,s in parts])
# cluster: buffer 150 m
b=agr.buffer(150)
comps=list(b.geoms) if b.geom_type=='MultiPolygon' else [b]
rows=[]
for c in comps:
    a=agr.intersection(c)
    ha=a.area/1e4
    if ha<3: continue
    cen=a.centroid
    r={'ha':round(ha,1),'x':round(cen.x),'y':round(cen.y)}
    for k,u in OV.items():
        r[k]=round(a.intersection(u).area/a.area*100,1)
    free=a.difference(unary_union([OV['GNN'],OV['GOZ'],OV['N2000'],OV['N-reductie'],OV['NatteLandnatuur']]))
    r['vrij_ha']=round(free.area/1e4,1)
    # locatieserver reverse
    try:
        q=urllib.parse.urlencode({'type':'adres','rows':'1','X':str(cen.x),'Y':str(cen.y),'fl':'weergavenaam,woonplaatsnaam,buurtnaam'})
        j=json.load(urllib.request.urlopen(urllib.request.Request('https://api.pdok.nl/bzk/locatieserver/search/v3_1/reverse?'+q,headers={'User-Agent':'Mozilla/5.0'}),timeout=60))
        d=j['response']['docs'][0]; r['naam']=d.get('weergavenaam'); 
    except Exception as e: r['naam']='?'
    rows.append(r)
rows.sort(key=lambda r:-r['ha'])
for r in rows: print(r)
json.dump(rows,open('deelgebieden_out.json','w'),indent=1,ensure_ascii=False)
