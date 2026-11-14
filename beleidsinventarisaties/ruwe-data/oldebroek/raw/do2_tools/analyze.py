import json, sys, os
from shapely.geometry import shape, mapping, Point
from shapely.ops import unary_union
from shapely.validation import make_valid
from shapely.prepared import prep
G=sys.argv[1]; OUT=sys.argv[2]
def load(name, filt=None):
    d=json.load(open(os.path.join(G,name+".geojson")))
    gs=[make_valid(shape(f["geometry"])) for f in d["features"] if f.get("geometry") and (not filt or filt(f["properties"]))]
    return unary_union(gs) if gs else None
gem=load("kadaster_gemeentegebied_bbox",lambda p:p.get("code")=="0269")
res={"gemeente_ha":gem.area/1e4}
brp=json.load(open(os.path.join(G,"pdok_brp.geojson")))
agr=[];cats={}
for f in brp["features"]:
    p=f["properties"]; cat=p.get("category")
    if cat in("Natuurterrein","Landschapselement"): continue
    g=make_valid(shape(f["geometry"]))
    if not g.intersects(gem): continue
    gi=g.intersection(gem); agr.append(gi); cats[cat]=cats.get(cat,0)+gi.area/1e4
agr_u=unary_union(agr); res["brp_landbouw_ha"]=agr_u.area/1e4; res["brp_cats"]=cats
ov={
 "GNN":load("POVE_Gelders_natuurnetwerk"),
 "GOZ":load("POVE_Groene_ontwikkelingszone"),
 "Weidevogel":load("POVE_Weidevogelgebieden"),
 "Ganzenrust":load("POVE_Ganzenrustgebieden"),
 "Natte landnatuur":load("POVE_Beschzones_nat_landnat"),
 "N2000 alle":load("pdok_natura2000"),
 "N2000 Veluwe":load("pdok_natura2000",lambda p:p["naamN2K"]=="Veluwe"),
 "N2000 Veluwerandmeren":load("pdok_natura2000",lambda p:p["naamN2K"]=="Veluwerandmeren"),
 "N2000 Rijntakken":load("pdok_natura2000",lambda p:p["naamN2K"]=="Rijntakken"),
 "Stikstof beperkingengebied":load("ngr_d_Pvbb_Stikstofemissie_beperkingengebied"),
 "Nationaal landschap Veluwe":load("POVE_Nationale_landschappen"),
 "Streek Veluwe":load("POVE_Streekgebieden",lambda p:p["streekgebied_naam"]=="Veluwe"),
 "Streek Randmeerkust":load("POVE_Streekgebieden",lambda p:p["streekgebied_naam"]=="Randmeerkust"),
 "Streek IJsselvallei":load("POVE_Streekgebieden",lambda p:p["streekgebied_naam"]=="IJsselvallei"),
 "Waterwingebied":load("POVE_Waterwingebieden"),
 "Grondwaterbescherming":load("POVE_Grondwaterbescherming"),
 "Intrekgebied":load("POVE_Intrekgebieden"),
 "Drinkwaterreservering ASV":load("POVE_Drinkwaterreservering_ASV"),
 "Molenbiotoop":load("POVE_Molenbiotoop"),
 "Molenbiotoop (ngr_a)":load("ngr_a_ChAr_Molenbiotoop"),
 "Stiltegebied":load("POVE_Stiltegebieden"),
 "Ammoniakbuffergebied":load("POVE_Ammoniakbuffergebied"),
 "Oude bosgroeiplaatsen":load("POVE_Oude_bosgroeiplaatsen"),
 "Windturbines verbod Veluwe":load("POVE_Windturbines_verbodsgebied_Veluwe"),
 "Zorgplicht provinciale weg":load("POVE_Provinciale_weg_zorgplichtgebied"),
 "Aardkundige waarde":load("ngr_a_Ab_Aardkundige_waarde"),
 "Glastuinbouw (buiten ontw.gebied)":load("POVE_Glastuinbouw"),
 "Weidevogel (POVI visie)":load("ngr_visie_POVI_Weidevogelgebieden"),
}
for nm in ["Polder Oldebroek","Polder Oosterwolde","Broeklanden","Randmeerkust-Polder Het Goor","Bentinkswellen"]:
    ov["WV: "+nm]=load("POVE_Weidevogelgebieden",lambda p,nm=nm:p["gebiedsnaam"]==nm)
ov["GNN of GOZ"]=unary_union([ov["GNN"],ov["GOZ"]])
nat=[ov[k] for k in["GNN","GOZ","N2000 alle","Weidevogel","Ganzenrust"]]
ov["Natuur/vogeloverlay (GNN/GOZ/N2000/WV/GR)"]=unary_union(nat)
ov["Idem + stikstofstrook + natte landnatuur"]=unary_union(nat+[ov["Stikstof beperkingengebied"],ov["Natte landnatuur"]])
rows=[]
for k,g in ov.items():
    if g is None: rows.append((k,0,0,0,0)); continue
    gm=g.intersection(gem).area/1e4; ga=g.intersection(agr_u).area/1e4
    rows.append((k,gm,100*gm/res["gemeente_ha"],ga,100*ga/res["brp_landbouw_ha"]))
res["rows"]=rows
print("gemeente ha %.1f; BRP landbouw ha %.1f"%(res["gemeente_ha"],res["brp_landbouw_ha"]),{k:round(v,1) for k,v in cats.items()})
print("| Overlay | ha gemeente | % gemeente | ha landbouw | % landbouw |")
for r in rows: print("| %s | %.1f | %.1f | %.1f | %.1f |"%r)
free=agr_u.difference(ov["Idem + stikstofstrook + natte landnatuur"])
res["free_ha"]=free.area/1e4
free2=agr_u.difference(unary_union([ov["GNN"],ov["GOZ"],ov["Weidevogel"],ov["Ganzenrust"]]))
res["free_gnn_goz_wv_gr_ha"]=free2.area/1e4
print("vrij (buiten alle natuur/vogel/stikstof/nat): %.1f ha (%.1f%%); buiten GNN/GOZ/WV/GR: %.1f ha"%(res["free_ha"],100*res["free_ha"]/res["brp_landbouw_ha"],res["free_gnn_goz_wv_gr_ha"]))
# kernen
kn=json.load(open(os.path.join(G,"cbs_bevolkingskernen.geojson")))
kernen={}
for f in kn["features"]:
    g=make_valid(shape(f["geometry"]))
    if gem.contains(g.representative_point()) and f["properties"]["provincie"]=="Gelderland":
        nm=f["properties"]["naam2021"]
        if nm in("Hoge Enk","'t Harde","Heerde-Kern","Heerde-Bakhuisbos","Hattem","Elburg"): continue
        kernen[nm]=(g,f["properties"]["aantalInwoners"],f["properties"]["aantalWoningenBag"])
res["kernen"]={}
sel={"GNN":ov["GNN"],"GOZ":ov["GOZ"],"WV":ov["Weidevogel"],"GR":ov["Ganzenrust"],"N2000":ov["N2000 alle"],"Stikstof":ov["Stikstof beperkingengebied"],"NatteLN":ov["Natte landnatuur"],"Waterwin":ov["Waterwingebied"],"Grondwb":ov["Grondwaterbescherming"],"Intrek":ov["Intrekgebied"],"Molen":unary_union([ov["Molenbiotoop"],ov["Molenbiotoop (ngr_a)"]]),"NLVeluwe":ov["Nationaal landschap Veluwe"],"Veluwe(streek)":ov["Streek Veluwe"],"Randmeerk":ov["Streek Randmeerkust"],"ASV":ov["Drinkwaterreservering ASV"],"Ammoniakbuffer":ov["Ammoniakbuffergebied"]}
allk=unary_union([v[0] for v in kernen.values()])
for nm,(g,inw,wo) in sorted(kernen.items(),key=lambda x:-x[1][1]):
    r={"inw":inw,"woningen":wo,"kern_ha":g.area/1e4}
    # overlays on the kern itself
    r["kern_overlay_pct"]={k:round(100*v.intersection(g).area/g.area,1) for k,v in sel.items() if v is not None and v.intersection(g).area>0}
    r["ringen"]={}
    prev=g
    for lo,hi in[(0,250),(250,500),(500,1000),(1000,2000)]:
        ring=g.buffer(hi).difference(g.buffer(lo)) if lo>0 else g.buffer(hi).difference(g)
        ring=ring.difference(allk) if nm else ring
        a=agr_u.intersection(ring)
        if a.area==0: r["ringen"][f"{lo}-{hi}"]={"landbouw_ha":0}; continue
        d={"landbouw_ha":round(a.area/1e4,1)}
        for k,v in sel.items():
            if v is None: continue
            d[k]=round(100*v.intersection(a).area/a.area,1)
        d["vrij_ha"]=round(free.intersection(ring).area/1e4,1)
        d["vrij_pct"]=round(100*free.intersection(ring).area/a.area,1)
        r["ringen"][f"{lo}-{hi}"]=d
    res["kernen"][nm]=r
json.dump(res,open(OUT,"w"),indent=1,default=float)
with open(OUT.replace(".json","_free.geojson"),"w") as f:
    cl=free.buffer(25).buffer(-25)
    parts=list(cl.geoms) if hasattr(cl,"geoms") else [cl]
    parts=sorted([p for p in parts if p.area>2e4],key=lambda p:-p.area)
    json.dump({"type":"FeatureCollection","features":[{"type":"Feature","properties":{"ha":p.area/1e4},"geometry":mapping(p)} for p in parts]},f)
for nm,r in res["kernen"].items():
    print("\n##",nm,r["inw"],"inw;",r["woningen"],"won; kern ha",round(r["kern_ha"],1),"kern-overlay:",r["kern_overlay_pct"])
    for ring,d in r["ringen"].items(): print("  ",ring,d)
