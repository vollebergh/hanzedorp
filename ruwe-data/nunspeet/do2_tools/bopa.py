import json, sys, os
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely.validation import make_valid
G=sys.argv[1]
def load(name, filt=None):
    d=json.load(open(os.path.join(G,name+".geojson")))
    gs=[make_valid(shape(f["geometry"])) for f in d["features"] if f.get("geometry") and (not filt or filt(f["properties"]))]
    return unary_union(gs) if gs else None
gem=load("kadaster_gemeentegebied_bbox",lambda p:p.get("code")=="0302")
brp=json.load(open(os.path.join(G,"pdok_brp.geojson")))
agr=[]
for f in brp["features"]:
    p=f["properties"]
    if p.get("category") in("Natuurterrein","Landschapselement"): continue
    g=make_valid(shape(f["geometry"]))
    if g.intersects(gem): agr.append(g.intersection(gem))
A=unary_union(agr); tot=A.area
ov={k:load(n) for k,n in [("GNN","POVE_Gelders_natuurnetwerk"),("GO","POVE_Groene_ontwikkelingszone"),("NatteLN","POVE_Beschzones_nat_landnat"),("WV","POVE_Weidevogelgebieden"),("NL","POVE_Nationale_landschappen"),("Molen","POVE_Molenbiotoop"),("Intrek","POVE_Intrekgebieden"),("Waterwin","POVE_Waterwingebieden"),("GWB","POVE_Grondwaterbescherming"),("Provweg","POVE_Provinciale_wegen")]}
def pct(g): return 100*g.intersection(A).area/tot
nl_buiten=ov["NL"].difference(unary_union([ov["GNN"],ov["GO"]]))
print("NL buiten GNN/GO %.1f%%"%pct(nl_buiten))
adv=unary_union([ov["GNN"],ov["GO"],ov["NatteLN"],ov["WV"],nl_buiten,ov["Molen"],ov["Intrek"],ov["Waterwin"],ov["GWB"]])
print("min 1 adviesgeval: %.1f%%  (%.1f ha)"%(pct(adv),adv.intersection(A).area/1e4))
adv2=unary_union([ov["GNN"],ov["GO"],ov["NatteLN"],ov["WV"],ov["Molen"],ov["Intrek"],ov["Waterwin"],ov["GWB"]])
print("zonder NL-buiten: %.1f%%"%pct(adv2))
print("Intrek %.1f"%pct(ov["Intrek"]),"Molen %.1f"%pct(ov["Molen"]))
# gebieden Randmeerkust vs Veluwe farmland and overlays within each streek
st=json.load(open(os.path.join(G,"POVE_Streekgebieden.geojson")))
for nm in ("Randmeerkust","Veluwe"):
    s=unary_union([make_valid(shape(f["geometry"])) for f in st["features"] if f["properties"]["streekgebied_naam"]==nm])
    a=A.intersection(s); 
    if a.area==0: continue
    print(nm,"farmland ha %.1f"%(a.area/1e4), "GNN/GO/WV share %.1f%%"%(100*unary_union([ov["GNN"],ov["GO"],ov["WV"]]).intersection(a).area/a.area), "GO %.1f"%(100*ov["GO"].intersection(a).area/a.area),"GNN %.1f"%(100*ov["GNN"].intersection(a).area/a.area),"WV %.1f"%(100*ov["WV"].intersection(a).area/a.area))
# distance of farmland to provincial road
pw=ov["Provweg"]
print("farmland within 50m of provincial road %.1f ha"%(A.intersection(pw.buffer(50)).area/1e4))
