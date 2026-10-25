import sys, json, collections, pickle
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/scripts')
from common import *
from shapely.validation import make_valid
from shapely.ops import unary_union
from shapely.strtree import STRtree
import shapely
gem=geom_of('heerde_gemeente.json')[0][1]
L,C=pickle.load(open(D+'layers.pkl','rb'))
d=load('brp25_heerde_bbox.json')
parc=[]
for f in d['features']:
    g=make_valid(shape(f['geometry']))
    if not g.intersects(gem): continue
    g=g.intersection(gem)
    if g.is_empty: continue
    p=f['properties']; parc.append((p['category'],p['gewas'],g))
def area(sel):
    gs=[g for c,gw,g in parc if sel(c,gw)]
    return unary_union(gs)
prod=area(lambda c,gw: c in ('Grasland','Bouwland'))
tot=area(lambda c,gw: True)
print('productief',round(prod.area/1e4,1),'totaal BRP',round(tot.area/1e4,1))
pickle.dump((prod,tot),open(D+'agri.pkl','wb'))
rows=[]
def pct(name,geom):
    a=prod.intersection(geom).area
    rows.append((name,a/1e4,100*a/prod.area, 100*geom.area/gem.area))
for k in ['GNN','GOZ','N2000','N2000_Veluwe','N2000_Rijntakken','Weidevogel','Ganzenrust','NatteLandnatuur','Stikstofstrook','NL_Veluwe','WaardevolOpen','Molenbiotoop','Intrekgebied','Stiltegebied','Streek_IJsselvallei','Streek_Veluwe','Ammoniakbuffer','OudeBosgroeiplaats','ZoekgebiedNieuweNatuur','EVZ','Aardkundig_internationaal','Aardkundig_alle','Belvoir','ArcheoParel','Grondwaterfluctuatie','WindVerbod','WindAandacht']:
    pct(k,L[k])
for k,v in C.items(): pct('C:'+k,v)
for r in rows: print(f"{r[0]:40s} ha={r[1]:8.1f}  %landbouw={r[2]:5.1f}  %gemeente={r[3]:5.1f}")
# vrij
for k in ['Vrij_hard','Vrij_alles_incl_WOG_molen','NatuurVogel','NatuurVogelStikstof','BOPA_advies_alles','BOPA_advies_zonder_NL']:
    a=prod.intersection(C[k]).area
    print(k,'binnen',round(a/1e4,1),'buiten',round((prod.area-a)/1e4,1), round(100*(prod.area-a)/prod.area,1))
# Alles vrij van alle (incl. NL)
allov=unary_union([C['Vrij_alles_incl_WOG_molen'],L['NL_Veluwe']])
print('buiten alle incl NL', round((prod.area-prod.intersection(allov).area)/1e4,1))
# per weidevogelgebied/ganzenrust naam
json.dump({r[0]:[r[1],r[2],r[3]] for r in rows},open(D+'agri_overlay_table.json','w'),indent=1)
