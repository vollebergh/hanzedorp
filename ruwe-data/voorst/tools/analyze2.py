"""Aanvullende kaartlagen (Waardevol open gebied, Leefgebied weidevogels, ganzenfoerageergebieden) + afstanden kernen tot Natura 2000/GNN. python3 -I analyze2.py <geodir> <out.json>"""
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
vo = load("kadaster_gemeentegebied_bbox", lambda p: p.get("code") == "0285"); pv = prep(vo)
brp = json.load(open(os.path.join(G, "pdok_brp.geojson")))
ag = unary_union([make_valid(shape(f["geometry"])).intersection(vo) for f in brp["features"]
    if f["properties"].get("category") not in ("Natuurterrein","Landschapselement") and pv.intersects(make_valid(shape(f["geometry"])))])
L = {"Waardevol open gebied (ikn, Ov.verordening)": load("ikn_Waardevolle_Open_gebieden"),
     "Leefgebied weidevogels (ikn, = weidevogelgebied)": load("ikn_Leefgebied_Weidevogels"),
     "Ganzenfoerageergebieden (ikn)": load("ikn_Ganzenfoerageergebieden_ook_wel_ganzenrustgebieden"),
     "Rustgebied winterganzen (visie)": load("ngr_visie_POVI_Rustgebied_winterganzen"),
     "Weidevogelgebied (visie POVI)": load("ngr_visie_POVI_Weidevogelgebieden"),
     "Weidevogelgebied (verordening POVE)": load("POVE_Weidevogelgebieden"),
     "Ganzenrustgebied (verordening POVE)": load("POVE_Ganzenrustgebieden")}
res = {"rows": []}
for k, g in L.items():
    gm = g.intersection(vo).area/1e4; ga = g.intersection(ag).area/1e4
    res["rows"].append((k, gm, 100*gm/(vo.area/1e4), ga, 100*ga/(ag.area/1e4)))
    print("| %s | %.1f | %.1f | %.1f | %.1f |" % res["rows"][-1])
# afstanden kernen
bu = json.load(open(os.path.join(G, "cbs_buurten_voorst.geojson")))
B = {f["properties"]["buurtcode"]: make_valid(shape(f["geometry"])) for f in bu["features"]}
kernen = {"Twello": ["BU02850100","BU02850101","BU02850102"], "Steenenkamer":["BU02850106"], "Voorst":["BU02850000"], "Terwolde":["BU02850103"], "Nijbroek":["BU02850104"],
 "Klarenbeek (Voorster deel)":["BU02850200"], "Teuge":["BU02850201"], "Wilp":["BU02850300"], "Posterenk":["BU02850301"], "Wilp-Achterhoek":["BU02850202"],"De Vecht":["BU02850203"],"Bussloo":["BU02850001"],"Gietelo":["BU02850002"]}
n2k = {n: load("pdok_natura2000", lambda p, n=n: p.get("naamN2K")==n) for n in ("Veluwe","Rijntakken","Landgoederen Brummen")}
gnn = load("POVE_Gelders_natuurnetwerk"); goz = load("POVE_Groene_ontwikkelingszone"); wov = L["Waardevol open gebied (ikn, Ov.verordening)"]
print("kern | d_Veluwe_N2000 | d_Rijntakken | d_LgBrummen | d_GNN | d_GOZ | d_WaardevolOpen(m)")
res["afstanden"] = {}
for k, c in kernen.items():
    kg = unary_union([B[x] for x in c])
    d = [round(kg.distance(n2k[n])) for n in ("Veluwe","Rijntakken","Landgoederen Brummen")] + [round(kg.distance(gnn)), round(kg.distance(goz)), round(kg.distance(wov))]
    res["afstanden"][k] = d; print(k, "|", " | ".join(map(str, d)))
json.dump(res, open(OUT, "w"), indent=1, default=float)
