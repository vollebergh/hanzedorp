# DO2 Harderwijk: agrarische grond (BRP 2025 excl. natuurterrein/overige) binnen ringen rond kernen (CBS Bevolkingskernen 2021); "vrij" = buiten GNN, GOZ, N2000, stikstofreductiegebied, natte landnatuur
import json, os
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely import make_valid
D='data'; W=D+'/wfs'
G=shape(json.load(open(D+'/harderwijk_gemeente_gm.json'))['features'][0]['geometry'])
def L(fn): return [(f['properties'],make_valid(shape(f['geometry']))) for f in json.load(open(fn))['features']]
def lay(fn): return make_valid(unary_union([s for p,s in L(os.path.join(W,fn))])).intersection(G)
OV={'GNN':lay('Gelders_natuurnetwerk.json'),'GOZ':lay('Groene_ontwikkelingszone.json'),'Natte':lay('Beschzones_nat_landnat.json'),'Nred':lay('Stikstofreductiegebied.json'),'Intrek':lay('Intrekgebieden.json')}
OV['N2000']=make_valid(unary_union([s for p,s in L(D+'/pdok/natura2000.json')])).intersection(G)
brp=[(f['properties'],make_valid(shape(f['geometry']))) for f in json.load(open(D+'/pdok/brp2025.json'))['features']]
agr=unary_union([s.intersection(G) for p,s in brp if p['category'] not in('Natuurterrein','Overige') and s.intersects(G)])
vrij=agr.difference(unary_union([OV['GNN'],OV['GOZ'],OV['N2000'],OV['Nred'],OV['Natte']]))
kern={p['naam2021']:s for p,s in L(D+'/pdok/kernen2021.json') if p['naam2021'] in ('Harderwijk (Gld.)','Hierden-Kern','Hierden-De Biest','Harderwijk-Drielanden','Harderwijk-Zuid','Sonnevanck')}
kern['Hierden (Kern+De Biest)']=unary_union([kern['Hierden-Kern'],kern['Hierden-De Biest']])
print('%-26s %6s %8s %8s %8s %8s'%('Kern','ring m','agr ha','vrij ha','GOZ%','GNN%'))
for n in ['Harderwijk (Gld.)','Harderwijk-Drielanden','Hierden (Kern+De Biest)','Hierden-Kern','Hierden-De Biest']:
    for r in (0,100,250,500,1000):
        z=kern[n].buffer(r) if r else kern[n]
        a=agr.intersection(z); v=vrij.intersection(z); ha=a.area/1e4
        print('%-26s %6d %8.1f %8.1f %8.1f %8.1f'%(n,r,ha,v.area/1e4,(a.intersection(OV['GOZ']).area/a.area*100 if ha else 0),(a.intersection(OV['GNN']).area/a.area*100 if ha else 0)))
