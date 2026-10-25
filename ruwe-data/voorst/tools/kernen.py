"""Kernen-analyse Voorst: per kern (CBS-buurten 2024 als bebouwde kern) de overlay-belasting van productieve landbouwgrond
binnen 0-250 m en 250-500 m van de kern. python3 -I kernen.py <geodir> <out.json>"""
import json, sys, os
from shapely.geometry import shape, Point
from shapely.ops import unary_union
from shapely.validation import make_valid
from shapely.prepared import prep
G, OUT = sys.argv[1], sys.argv[2]
def load(name, filt=None):
    d = json.load(open(os.path.join(G, name + ".geojson")))
    gs = [make_valid(shape(f["geometry"])) for f in d["features"] if f.get("geometry") and (not filt or filt(f["properties"]))]
    return unary_union(gs) if gs else None
vo = load("kadaster_gemeentegebied_bbox", lambda p: p.get("code") == "0285")
pv = prep(vo)
# BRP productief
brp = json.load(open(os.path.join(G, "pdok_brp.geojson")))
ag = []
for f in brp["features"]:
    p = f["properties"]
    if p.get("category") in ("Natuurterrein", "Landschapselement"): continue
    g = make_valid(shape(f["geometry"]))
    if pv.intersects(g): ag.append(g.intersection(vo))
ag = unary_union(ag)
ov = {
 "GNN": load("POVE_Gelders_natuurnetwerk"), "GOZ": load("POVE_Groene_ontwikkelingszone"),
 "Weidevogel": load("POVE_Weidevogelgebieden"), "Ganzenrust": load("POVE_Ganzenrustgebieden"),
 "N2000": load("pdok_natura2000"), "NatteLandnatuur": load("POVE_Beschzones_nat_landnat"),
 "Waterwin": load("POVE_Waterwingebieden"), "Molenbiotoop": load("POVE_Molenbiotoop"),
 "Boringsvrij": load("POVE_Boringsvrije_zone"), "ASV_drinkwaterres": load("POVE_Drinkwaterreservering_ASV"),
 "Ammoniakbuffer": load("POVE_Ammoniakbuffergebied"), "OudeBosgroeiplaats": load("POVE_Oude_bosgroeiplaatsen"),
 "ProvWegZorgplicht": load("POVE_Provinciale_weg_zorgplichtgebied"),
}
hard = unary_union([ov[k] for k in ("GNN", "N2000", "Waterwin") if ov[k] is not None])
cond = unary_union([ov[k] for k in ("GOZ", "Weidevogel", "Ganzenrust", "NatteLandnatuur") if ov[k] is not None])
# kernen
bu = json.load(open(os.path.join(G, "cbs_buurten_voorst.geojson")))
B = {f["properties"]["buurtcode"]: make_valid(shape(f["geometry"])) for f in bu["features"]}
nm = {f["properties"]["buurtcode"]: f["properties"]["buurtnaam"] for f in bu["features"]}
kernen = {
 "Twello (Midden/Zuid/Noord)": ["BU02850100", "BU02850101", "BU02850102"], "Steenenkamer": ["BU02850106"],
 "Voorst": ["BU02850000"], "Terwolde": ["BU02850103"], "Nijbroek": ["BU02850104"],
 "Klarenbeek (Voorster deel)": ["BU02850200"], "Teuge": ["BU02850201"], "Wilp": ["BU02850300"],
 "Posterenk": ["BU02850301"], "Wilp-Achterhoek": ["BU02850202"], "De Vecht": ["BU02850203"],
 "Bussloo": ["BU02850001"], "Gietelo": ["BU02850002"],
}
# woningen BAG
w = json.load(open(os.path.join(G, "bag_woningen_voorst.geojson")))
pts = [Point(f["geometry"]["coordinates"]) for f in w["features"]]
allkern = unary_union([B[c] for v in kernen.values() for c in v])
res = {"ag_ha": ag.area / 1e4, "kernen": {}}
def share(a, g): 
    return 100 * a.intersection(g).area / a.area if (g is not None and a.area > 0) else 0.0
for k, codes in kernen.items():
    kg = unary_union([B[c] for c in codes])
    nw = sum(1 for p in pts if kg.contains(p))
    out = {"woningen_in_kern": nw, "kern_ha": kg.area / 1e4}
    for lbl, (r0, r1) in {"0-250m": (0, 250), "250-500m": (250, 500)}.items():
        ring = kg.buffer(r1).difference(kg.buffer(r0) if r0 else kg).difference(allkern)
        a = ring.intersection(ag)
        d = {"ag_ha": a.area / 1e4}
        if a.area > 0:
            for o in ov: d[o] = round(share(a, ov[o]), 1)
            d["hard(GNN/N2000/waterwin)"] = round(share(a, hard), 1)
            d["voorwaardelijk(GOZ/wv/gr/nln)"] = round(share(a, cond), 1)
            d["geen_van_beide"] = round(100 - share(a, unary_union([hard, cond])), 1)
            d["vrij_ha"] = round(a.difference(unary_union([hard, cond])).area / 1e4, 1)
        out[lbl] = d
    res["kernen"][k] = out
json.dump(res, open(OUT, "w"), indent=1, default=float)
print("kern | won | kern_ha | ring | ag_ha | GNN GOZ WV GR N2000 NLN WW MOL BOR ASV AMM | hard | vw | vrij% | vrij_ha")
for k, o in res["kernen"].items():
    for lbl in ("0-250m", "250-500m"):
        d = o[lbl]
        if d["ag_ha"] <= 0: print(k, o["woningen_in_kern"], lbl, "geen landbouwgrond"); continue
        print(k, "|", o["woningen_in_kern"], "|", round(o["kern_ha"]), "|", lbl, "|", round(d["ag_ha"], 1), "|",
              d["GNN"], d["GOZ"], d["Weidevogel"], d["Ganzenrust"], d["N2000"], d["NatteLandnatuur"], d["Waterwin"], d["Molenbiotoop"], d["Boringsvrij"], d["ASV_drinkwaterres"], d["Ammoniakbuffer"], "|",
              d["hard(GNN/N2000/waterwin)"], d["voorwaardelijk(GOZ/wv/gr/nln)"], d["geen_van_beide"], d["vrij_ha"])
