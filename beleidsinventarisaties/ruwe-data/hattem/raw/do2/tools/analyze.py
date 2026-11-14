"""Overlay analysis Hattem. Usage: python3 -I analyze.py <geodir> <outjson> [landbouw|alle]"""
import json, sys, os
from shapely.geometry import shape, mapping
from shapely.ops import unary_union
from shapely.validation import make_valid

G = sys.argv[1]
OUT = sys.argv[2]
MODE = sys.argv[3] if len(sys.argv) > 3 else "landbouw"  # "landbouw" (excl. Natuurterrein/Landschapselement) or "alle" (alle BRP-percelen)


def load(name, filt=None):
    fn = os.path.join(G, name + ".geojson")
    d = json.load(open(fn))
    gs = []
    for f in d["features"]:
        if f.get("geometry") is None:
            continue
        if filt and not filt(f["properties"]):
            continue
        g = make_valid(shape(f["geometry"]))
        gs.append(g)
    if not gs:
        return None
    u = unary_union(gs)
    return u


# Hattem (Kadaster bestuurlijke gebieden, actueel) and CBS 2024 check
ham = load("kadaster_gemeentegebied_bbox", lambda p: p.get("code") == "0244")
ham_cbs = load("cbs2024_gemeenten_bbox", lambda p: p.get("statcode") == "GM0244")
res = {"gemeente_ha_kadaster": ham.area / 1e4, "gemeente_ha_cbs2024": ham_cbs.area / 1e4,
       "symdiff_ha": ham.symmetric_difference(ham_cbs).area / 1e4}

# BRP 2025 landbouw (excl. Natuurterrein, Landschapselement en natuur-gewassen)
brp = json.load(open(os.path.join(G, "pdok_brp.geojson")))
agr, cats = [], {}
for f in brp["features"]:
    p = f["properties"]
    cat = p.get("category")
    gew = (p.get("gewas") or "").lower()
    if MODE == "landbouw" and cat in ("Natuurterrein", "Landschapselement"):
        continue
    g = make_valid(shape(f["geometry"]))
    if not g.intersects(ham):
        continue
    gi = g.intersection(ham)
    agr.append(gi)
    cats[cat] = cats.get(cat, 0) + gi.area / 1e4
agr_u = unary_union(agr)
res["brp_landbouw_ha"] = agr_u.area / 1e4
res["brp_cats_ha"] = cats

ov = {
    "GNN": load("POVE_Gelders_natuurnetwerk"),
    "GOZ": load("POVE_Groene_ontwikkelingszone"),
    "Weidevogel (verordening)": load("POVE_Weidevogelgebieden"),
    "Ganzenrust": load("POVE_Ganzenrustgebieden"),
    "Natte landnatuur (beschermingszone)": load("POVE_Beschzones_nat_landnat"),
    "Natura 2000 (alle)": load("pdok_natura2000"),
    "N2000 Veluwe": load("pdok_natura2000", lambda p: p.get("naamN2K") == "Veluwe"),
    "N2000 Rijntakken": load("pdok_natura2000", lambda p: p.get("naamN2K") == "Rijntakken"),
    "Beperkingengebied stikstofemissie": load("ngr_d_Pvbb_Stikstofemissie_beperkingengebied"),
    "Nationaal landschap Veluwe": load("POVE_Nationale_landschappen"),
    "Streek Veluwe": load("POVE_Streekgebieden", lambda p: p.get("streekgebied_naam") == "Veluwe"),
    "Streek IJsselvallei": load("POVE_Streekgebieden", lambda p: p.get("streekgebied_naam") == "IJsselvallei"),
    "Streek Randmeerkust": load("POVE_Streekgebieden", lambda p: p.get("streekgebied_naam") == "Randmeerkust"),
    "Waterwingebied": load("POVE_Waterwingebieden"),
    "Grondwaterbeschermingsgebied": load("POVE_Grondwaterbescherming"),
    "Boringsvrije zone": load("POVE_Boringsvrije_zone"),
    "Intrekgebied": load("POVE_Intrekgebieden"),
    "Drinkwaterreservering (ASV)": load("POVE_Drinkwaterreservering_ASV"),
    "Molenbiotoop": load("POVE_Molenbiotoop"),
    "Ammoniakbuffergebied": load("POVE_Ammoniakbuffergebied"),
    "Oude bosgroeiplaatsen": load("POVE_Oude_bosgroeiplaatsen"),
    "Windturbines verbodsgebied Veluwe": load("POVE_Windturbines_verbodsgebied_Veluwe"),
    "Zorgplicht provinciale weg": load("POVE_Provinciale_weg_zorgplichtgebied"),
    "Aardkundige waarde (niet-verordening)": load("ngr_a_Ab_Aardkundige_waarde"),
}
for nm in ["Bentinkswellen", "Gelderdijksche Waard", "Hoenwaard", "Wapenveldsche Broek"]:
    ov["Weidevogel: " + nm] = load("POVE_Weidevogelgebieden", lambda p, nm=nm: p.get("gebiedsnaam") == nm)

ov["GNN of GOZ"] = unary_union([ov["GNN"], ov["GOZ"]])
nat = [ov[k] for k in ["GNN", "GOZ", "Natura 2000 (alle)", "Weidevogel (verordening)", "Ganzenrust"] if ov[k] is not None]
ov["Natuur- of vogeloverlay (GNN/GOZ/N2000/weidevogel/ganzenrust)"] = unary_union(nat)
ov["Idem + stikstofstrook + natte landnatuur"] = unary_union(
    nat + [ov["Beperkingengebied stikstofemissie"], ov["Natte landnatuur (beschermingszone)"]])

rows = []
for k, g in ov.items():
    if g is None:
        rows.append((k, 0, 0, 0, 0))
        continue
    gm = g.intersection(ham).area / 1e4
    ga = g.intersection(agr_u).area / 1e4
    rows.append((k, gm, 100 * gm / res["gemeente_ha_kadaster"], ga, 100 * ga / res["brp_landbouw_ha"]))
res["rows"] = rows

# Free agricultural land: BRP landbouw outside nature/bird overlays + stikstofstrook + natte landnatuur
free = agr_u.difference(ov["Idem + stikstofstrook + natte landnatuur"])
res["free_ha"] = free.area / 1e4
# Also outside GNN/GOZ/weidevogel/ganzenrust only (N2000 overlap mostly == GNN)
free2 = agr_u.difference(unary_union([ov["GNN"], ov["GOZ"], ov["Weidevogel (verordening)"], ov["Ganzenrust"]]))
res["free_excl_gnn_goz_wv_gr_ha"] = free2.area / 1e4
# within IJsselvallei / Veluwe
for s in ["Streek IJsselvallei", "Streek Veluwe"]:
    res["free_in_" + s] = free.intersection(ov[s]).area / 1e4
# clusters of free land (buffer 25 m to join adjacent parcels)
cl = free.buffer(25).buffer(-25)
parts = list(cl.geoms) if hasattr(cl, "geoms") else [cl]
parts = sorted([p for p in parts if p.area > 2e4], key=lambda p: -p.area)
res["free_clusters"] = [{"ha": round(p.area / 1e4, 1), "cx": round(p.centroid.x), "cy": round(p.centroid.y),
                         "bounds": [round(b) for b in p.bounds],
                         "in_molenbiotoop": bool(ov["Molenbiotoop"] and p.intersects(ov["Molenbiotoop"])),
                         "in_boringsvrij": bool(ov["Boringsvrije zone"] and p.intersects(ov["Boringsvrije zone"])),
                         "streek": [s for s in ["Streek IJsselvallei", "Streek Veluwe"] if p.intersection(ov[s]).area > 0.5 * p.area]}
                        for p in parts[:25]]
json.dump(res, open(OUT, "w"), indent=1, default=float)
with open(OUT.replace(".json", "_free.geojson"), "w") as f:
    json.dump({"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"ha": p.area / 1e4},
                                                          "geometry": mapping(p)} for p in parts]}, f)

print("gemeente ha kadaster %.1f cbs2024 %.1f symdiff %.2f" % (res["gemeente_ha_kadaster"], res["gemeente_ha_cbs2024"], res["symdiff_ha"]))
print("BRP landbouw ha %.1f" % res["brp_landbouw_ha"], {k: round(v, 1) for k, v in cats.items()})
print("| Overlay | ha in gemeente | % gemeente | ha landbouw (BRP) | % landbouw |")
for r in rows:
    print("| %s | %.1f | %.1f | %.1f | %.1f |" % r)
print("free ha", round(res["free_ha"], 1), "free2", round(res["free_excl_gnn_goz_wv_gr_ha"], 1),
      {k: round(v, 1) for k, v in res.items() if k.startswith("free_in_")})
for c in res["free_clusters"]:
    print(c)
