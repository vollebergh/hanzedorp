import json
from shapely.geometry import shape
from shapely.ops import unary_union
D='data'; W=D+'/wfs'
G=shape(json.load(open(D+'/ermelo_gemeente_gm.json'))['features'][0]['geometry'])
brp=[(f['properties'],shape(f['geometry']).buffer(0)) for f in json.load(open(D+'/pdok/brp2025.json'))['features']]
agr=unary_union([s.intersection(G) for p,s in brp if p['category'] not in('Natuurterrein','Overige') and s.intersects(G)])
def lay(fn,filt=None):
    return unary_union([shape(f['geometry']).buffer(0) for f in json.load(open(fn))['features'] if (filt is None or filt(f['properties']))]).intersection(G)
st={n:lay(W+'/Streekgebieden.json',lambda p,n=n:p['streekgebied_naam']==n) for n in('Veluwe','Randmeerkust')}
OV={'GNN':lay(W+'/Gelders_natuurnetwerk.json'),'GOZ':lay(W+'/Groene_ontwikkelingszone.json'),'N2000':lay(D+'/pdok/natura2000.json'),'Natte landnatuur':lay(W+'/Beschzones_nat_landnat.json'),
    'Intrekgebied':lay(W+'/Intrekgebieden.json'),'Stikstofreductiegebied':lay(W+'/Stikstofreductiegebied.json'),'Ammoniakbuffer':lay(W+'/Ammoniakbuffergebied.json'),'NL Veluwe':lay(W+'/Nationale_landschappen.json')}
natuur=unary_union([OV[k] for k in('GNN','GOZ','N2000')])
res={}
for n,s in st.items():
    a=agr.intersection(s); r={'agr_ha':round(a.area/1e4,1)}
    for k,o in OV.items(): r[k]=round(a.intersection(o).area/a.area*100,1)
    r['GNN of GOZ of N2000']=round(a.intersection(natuur).area/a.area*100,1)
    r['vrij (GNN/GOZ/N2000/stikstof)']=round(a.difference(unary_union([natuur,OV['Stikstofreductiegebied']])).area/a.area*100,1)
    res[n]=r; print(n,r)
json.dump(res,open(D+'/deelgebieden.json','w'),indent=1)
