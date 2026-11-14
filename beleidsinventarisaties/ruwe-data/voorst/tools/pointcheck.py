"""Puntcontrole: geocodeer adressen (PDOK Locatieserver) en toets ligging in provinciale overlays. python3 -I pointcheck.py <geodir> <outjson>"""
import json, sys, os, urllib.request, urllib.parse
from shapely.geometry import shape, Point
from shapely.ops import unary_union
from shapely.validation import make_valid
G, OUT = sys.argv[1], sys.argv[2]
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
def load(name, filt=None):
    d = json.load(open(os.path.join(G, name + ".geojson")))
    gs = [make_valid(shape(f["geometry"])) for f in d["features"] if f.get("geometry") and (not filt or filt(f["properties"]))]
    return unary_union(gs) if gs else None
ov = {"GNN": load("POVE_Gelders_natuurnetwerk"), "GOZ": load("POVE_Groene_ontwikkelingszone"), "WV": load("POVE_Weidevogelgebieden"),
 "GR": load("POVE_Ganzenrustgebieden"), "N2000": load("pdok_natura2000"), "NLN": load("POVE_Beschzones_nat_landnat"),
 "WW": load("POVE_Waterwingebieden"), "MOL": load("POVE_Molenbiotoop"), "NL-Veluwe": load("POVE_Nationale_landschappen"),
 "ASV": load("POVE_Drinkwaterreservering_ASV"), "BOR": load("POVE_Boringsvrije_zone"), "AMM": load("POVE_Ammoniakbuffergebied"),
 "OBG": load("POVE_Oude_bosgroeiplaatsen"), "STIKSTOF500": load("ngr_d_Pvbb_Stikstofemissie_beperkingengebied")}
vo = load("kadaster_gemeentegebied_bbox", lambda p: p.get("code") == "0285")
Q = json.load(open(sys.argv[3]))
res = []
for label, q in Q:
    u = "https://api.pdok.nl/bzk/locatieserver/search/v3_1/free?" + urllib.parse.urlencode({"q": q, "rows": 1, "fq": "type:adres", "fl": "weergavenaam,centroide_rd,gemeentenaam"})
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60).read())["response"]["docs"]
    if not d: res.append({"label": label, "q": q, "fout": "niet gevonden"}); continue
    x, y = [float(v) for v in d[0]["centroide_rd"].replace("POINT(", "").replace(")", "").split()]
    p = Point(x, y)
    r = {"label": label, "adres": d[0]["weergavenaam"], "gemeente": d[0]["gemeentenaam"], "rd": [round(x), round(y)]}
    r["overlays"] = [k for k, g in ov.items() if g is not None and g.contains(p)]
    r["dist_stikstofstrook_m"] = round(ov["STIKSTOF500"].distance(p)) if ov["STIKSTOF500"] is not None else None
    r["dist_GOZ_m"] = round(ov["GOZ"].distance(p)) if ov["GOZ"] is not None and not ov["GOZ"].contains(p) else 0
    res.append(r)
json.dump(res, open(OUT, "w"), indent=1, ensure_ascii=False)
for r in res:
    print(r.get("label"), "|", r.get("adres", r.get("fout")), "|", r.get("rd"), "|", ",".join(r.get("overlays", [])), "| d_GOZ", r.get("dist_GOZ_m"), "| d_N", r.get("dist_stikstofstrook_m"))
