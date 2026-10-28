# DO2 Harderwijk: agrarische grond (BRP 2025, excl. natuurterrein/overige) per CBS-buurt (2024) met overlay-druk
import json, os
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely import make_valid
D='data'; W=D+'/wfs'
G=shape(json.load(open(D+'/harderwijk_gemeente_gm.json'))['features'][0]['geometry'])
def L(fn):
    return [(f['properties'],make_valid(shape(f['geometry']))) for f in json.load(open(fn))['features']]
def lay(fn): return make_valid(unary_union([s for p,s in L(os.path.join(W,fn))])).intersection(G)
OV={'GNN':lay('Gelders_natuurnetwerk.json'),'GOZ':lay('Groene_ontwikkelingszone.json'),'NatteLandnatuur':lay('Beschzones_nat_landnat.json'),'N-reductie':lay('Stikstofreductiegebied.json'),'NL Veluwe':lay('Nationale_landschappen.json'),'Intrek':lay('Intrekgebieden.json')}
OV['N2000']=make_valid(unary_union([s for p,s in L(D+'/pdok/natura2000.json')])).intersection(G)
brp=[(f['properties'],make_valid(shape(f['geometry']))) for f in json.load(open(D+'/pdok/brp2025.json'))['features']]
agr=unary_union([s.intersection(G) for p,s in brp if p['category'] not in('Natuurterrein','Overige') and s.intersects(G)])
vrij_set=unary_union([OV['GNN'],OV['GOZ'],OV['N2000'],OV['N-reductie'],OV['NatteLandnatuur']])
rows=[]
for p,s in L(D+'/pdok/buurten2024.json'):
    if p['gemeentenaam']!='Harderwijk': continue
    a=agr.intersection(s)
    ha=a.area/1e4
    if ha<0.5: continue
    r={'buurt':p['buurtnaam'],'code':p['buurtcode'],'agr_ha':round(ha,1),'inw':p['aantalInwoners']}
    for k,u in OV.items(): r[k]=round(a.intersection(u).area/a.area*100,1)
    r['vrij_ha']=round(a.difference(vrij_set).area/1e4,1)
    rows.append(r)
rows.sort(key=lambda r:-r['agr_ha'])
tot=sum(r['agr_ha'] for r in rows)
for r in rows: print(r)
print('totaal',round(tot,1))
json.dump(rows,open('buurten_out.json','w'),indent=1,ensure_ascii=False)
