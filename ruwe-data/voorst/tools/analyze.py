"""Overlay-analyse gemeente Voorst (GM0285/0285). Usage: python3 -I analyze.py <geodir> <outjson> [landbouw|alle]
landbouw = BRP 2025 excl. Natuurterrein en Landschapselement (productieve landbouwgrond); alle = alle BRP-percelen."""
import json, sys, os
from shapely.geometry import shape, mapping
from shapely.ops import unary_union
from shapely.validation import make_valid
from shapely.prepared import prep
G, OUT = sys.argv[1], sys.argv[2]
MODE = sys.argv[3] if len(sys.argv) > 3 else "landbouw"

def load(name, filt=None):
    d = json.load(open(os.path.join(G, name + ".geojson")))
    gs = [make_valid(shape(f["geometry"])) for f in d["features"]
          if f.get("geometry") and (not filt or filt(f["properties"]))]
    return unary_union(gs) if gs else None

vo = load("kadaster_gemeentegebied_bbox", lambda p: p.get("code") == "0285")
vo_cbs = load("cbs2024_gemeenten_bbox", lambda p: p.get("statcode") == "GM0285")
res = {"gemeente_ha_kadaster": vo.area / 1e4, "gemeente_ha_cbs2024": vo_cbs.area / 1e4,
       "symdiff_ha": vo.symmetric_difference(vo_cbs).area / 1e4}
pv = prep(vo)
brp = json.load(open(os.path.join(G, "pdok_brp.geojson")))
agr, cats, seen = [], {}, set()
for f in brp["features"]:
    p = f["properties"]; cat = p.get("category")
    if MODE == "landbouw" and cat in ("Natuurterrein", "Landschapselement"):
        continue
    g = make_valid(shape(f["geometry"]))
    if not pv.intersects(g):
        continue
    gi = g.intersection(vo)
    agr.append(gi); cats[cat] = cats.get(cat, 0) + gi.area / 1e4
agr_u = unary_union(agr)
res["brp_ha"] = agr_u.area / 1e4; res["brp_cats_ha"] = cats
ov = {
 "GNN": load("POVE_Gelders_natuurnetwerk"),
 "GOZ": load("POVE_Groene_ontwikkelingszone"),
 "Weidevogel (verordening: Epseweerdse Polder-Wilpse Klei)": load("POVE_Weidevogelgebieden"),
 "Ganzenrust (IJsseluiterwaarden)": load("POVE_Ganzenrustgebieden"),
 "Natte landnatuur (beschermingszone)": load("POVE_Beschzones_nat_landnat"),
 "Natura 2000 (alle)": load("pdok_natura2000"),
 "N2000 Veluwe": load("pdok_natura2000", lambda p: p.get("naamN2K") == "Veluwe"),
 "N2000 Rijntakken": load("pdok_natura2000", lambda p: p.get("naamN2K") == "Rijntakken"),
 "N2000 Landgoederen Brummen": load("pdok_natura2000", lambda p: p.get("naamN2K") == "Landgoederen Brummen"),
 "Beperkingengebied stikstofemissie (voorbescherming)": load("ngr_d_Pvbb_Stikstofemissie_beperkingengebied"),
 "Nationaal landschap Veluwe": load("POVE_Nationale_landschappen"),
 "Streek IJsselvallei": load("POVE_Streekgebieden", lambda p: p.get("streekgebied_naam") == "IJsselvallei"),
 "Streek Veluwe": load("POVE_Streekgebieden", lambda p: p.get("streekgebied_naam") == "Veluwe"),
 "Streek Achterhoek": load("POVE_Streekgebieden", lambda p: p.get("streekgebied_naam") == "Achterhoek"),
 "Streek Randmeerkust": load("POVE_Streekgebieden", lambda p: p.get("streekgebied_naam") == "Randmeerkust"),
 "Waterwingebied (Twello)": load("POVE_Waterwingebieden"),
 "Grondwaterbeschermingsgebied": load("POVE_Grondwaterbescherming"),
 "Intrekgebied": load("POVE_Intrekgebieden"),
 "Boringsvrije zone": load("POVE_Boringsvrije_zone"),
 "Drinkwaterreservering (ASV Deventer-Zutphen)": load("POVE_Drinkwaterreservering_ASV"),
 "Molenbiotoop (verordening)": load("POVE_Molenbiotoop"),
 "Ammoniakbuffergebied": load("POVE_Ammoniakbuffergebied"),
 "Oude bosgroeiplaatsen": load("POVE_Oude_bosgroeiplaatsen"),
 "Windturbines verbodsgebied Veluwe": load("POVE_Windturbines_verbodsgebied_Veluwe"),
 "Zorgplichtgebied provinciale weg": load("POVE_Provinciale_weg_zorgplichtgebied"),
 "Glastuinbouw (verordening)": load("POVE_Glastuinbouw"),
 "Aardkundige waarde (niet-verordening)": load("ngr_a_Ab_Aardkundige_waarde"),
}
ov["GNN of GOZ"] = unary_union([x for x in (ov["GNN"], ov["GOZ"]) if x])
natk = ["GNN", "GOZ", "Natura 2000 (alle)", "Weidevogel (verordening: Epseweerdse Polder-Wilpse Klei)", "Ganzenrust (IJsseluiterwaarden)"]
nat = [ov[k] for k in natk if ov[k] is not None]
ov["Natuur- of vogeloverlay (GNN/GOZ/N2000/weidevogel/ganzenrust)"] = unary_union(nat)
ov["Idem + stikstofstrook + natte landnatuur + waterwin"] = unary_union(nat + [x for x in (ov["Beperkingengebied stikstofemissie (voorbescherming)"], ov["Natte landnatuur (beschermingszone)"], ov["Waterwingebied (Twello)"]) if x])
rows = []
for k, g in ov.items():
    if g is None: rows.append((k, 0, 0, 0, 0)); continue
    gm = g.intersection(vo).area / 1e4; ga = g.intersection(agr_u).area / 1e4
    rows.append((k, gm, 100 * gm / res["gemeente_ha_kadaster"], ga, 100 * ga / res["brp_ha"]))
res["rows"] = rows
free = agr_u.difference(ov["Idem + stikstofstrook + natte landnatuur + waterwin"])
res["free_ha"] = free.area / 1e4
free2 = agr_u.difference(unary_union([ov[k] for k in ["GNN","GOZ","Weidevogel (verordening: Epseweerdse Polder-Wilpse Klei)","Ganzenrust (IJsseluiterwaarden)"]]))
res["free_excl_gnn_goz_wv_gr_ha"] = free2.area / 1e4
res["goz_only_ha"] = agr_u.intersection(ov["GOZ"]).difference(unary_union([x for x in (ov["GNN"], ov["Weidevogel (verordening: Epseweerdse Polder-Wilpse Klei)"], ov["Ganzenrust (IJsseluiterwaarden)"], ov["Natura 2000 (alle)"]) if x])).area/1e4
json.dump(res, open(OUT, "w"), indent=1, default=float)
with open(OUT.replace(".json", "_free.geojson"), "w") as f:
    json.dump({"type":"FeatureCollection","features":[{"type":"Feature","properties":{"ha":free.area/1e4},"geometry":mapping(free)}]}, f)
print("gemeente ha kadaster %.1f cbs2024 %.1f symdiff %.2f" % (res["gemeente_ha_kadaster"], res["gemeente_ha_cbs2024"], res["symdiff_ha"]))
print("BRP ha %.1f" % res["brp_ha"], {k: round(v,1) for k,v in cats.items()})
print("| Overlay | ha gemeente | % gemeente | ha BRP | % BRP |")
for r in rows: print("| %s | %.1f | %.1f | %.1f | %.1f |" % r)
print("free", round(res["free_ha"],1), "free excl gnn/goz/wv/gr", round(res["free_excl_gnn_goz_wv_gr_ha"],1), "goz-only", round(res["goz_only_ha"],1))
