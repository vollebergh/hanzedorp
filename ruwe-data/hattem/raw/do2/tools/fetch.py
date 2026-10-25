"""Fetch Hattem boundary + Gelderland overlay layers + N2000 + BRP 2025 (EPSG:28992).
Usage: python3 -I fetch.py <outdir>
"""
import json, sys, os, urllib.request, urllib.parse

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read()


def wfs(base, typename, bbox=None, extra=None, version="2.0.0", count=None, start=None):
    p = {"service": "WFS", "request": "GetFeature", "version": version,
         "typeNames" if version.startswith("2") else "typeName": typename,
         "outputFormat": "application/json", "srsName": "EPSG:28992"}
    if bbox:
        p["bbox"] = ",".join(str(x) for x in bbox) + ",EPSG:28992"
    if count:
        p["count"] = str(count)
    if start is not None:
        p["startIndex"] = str(start)
    if extra:
        p.update(extra)
    url = base + "?" + urllib.parse.urlencode(p)
    return json.loads(get(url)), url


def save(name, data, url):
    with open(os.path.join(OUT, name + ".geojson"), "w") as f:
        json.dump(data, f)
    with open(os.path.join(OUT, "urls.txt"), "a") as f:
        f.write(f"{name}\t{len(data.get('features', []))}\t{url}\n")
    print(name, len(data.get("features", [])))


# 1. gemeentegrenzen (Hattem = GM0244); client-side filter
rough_bbox = (190000, 495000, 210000, 512000)
cbs = "https://service.pdok.nl/cbs/gebiedsindelingen/2024/wfs/v1_0"
d, u = wfs(cbs, "gebiedsindelingen:gemeente_niet_gegeneraliseerd", rough_bbox)
save("cbs2024_gemeenten_bbox", d, u)
kad = "https://service.pdok.nl/kadaster/bestuurlijkegebieden/wfs/v1_0"
d, u = wfs(kad, "bestuurlijkegebieden:Gemeentegebied", rough_bbox)
save("kadaster_gemeentegebied_bbox", d, u)

# Hattem bbox (approx, refined after first run) with margin
hb = (195500, 494500, 205000, 503500)  # Hattem bounds 196665,495307,203693,502628 + margin
gld = "https://geoserver.gelderland.nl/geoserver/ngr_verordening/wfs"
layers = ["POVE_Gelders_natuurnetwerk", "POVE_Groene_ontwikkelingszone", "POVE_Weidevogelgebieden",
          "POVE_Ganzenrustgebieden", "POVE_Beschzones_nat_landnat", "POVE_Nationale_landschappen",
          "POVE_Streekgebieden", "POVE_Waterwingebieden", "POVE_Grondwaterbescherming", "POVE_Intrekgebieden",
          "POVE_Boringsvrije_zone", "POVE_Molenbiotoop", "POVE_Stiltegebieden", "POVE_Ammoniakbuffergebied",
          "POVE_Oude_bosgroeiplaatsen", "POVE_Provinciale_wegen", "POVE_Provinciale_weg_zorgplichtgebied",
          "POVE_Windturbines_verbodsgebied_Veluwe", "POVE_Hollandse_Waterlinies", "POVE_Neder_Germaanse_limes",
          "POVE_Drinkwaterreservering_ASV", "POVE_KWO_vrije_zone", "POVE_Glastuinbouw", "POVE_Dijktrajecten"]
for l in layers:
    try:
        d, u = wfs(gld, "ngr_verordening:" + l, hb)
        save(l, d, u)
    except Exception as e:
        print("ERR", l, e)
for ws, l in [("ngr_d", "Pvbb_Stikstofemissie_beperkingengebied"), ("ngr_a", "Ab_Aardkundige_waarde"),
              ("ngr_a", "ChAr_Molenbiotoop"), ("ikn", "Nationaal_Landschap"), ("ngr_visie", "POVI_Weidevogelgebieden")]:
    try:
        d, u = wfs(f"https://geoserver.gelderland.nl/geoserver/{ws}/wfs", f"{ws}:{l}", hb)
        save(ws + "_" + l, d, u)
    except Exception as e:
        print("ERR", l, e)

# N2000
try:
    d, u = wfs("https://service.pdok.nl/rvo/natura2000/wfs/v1_0", "natura2000:natura2000", hb)
    save("pdok_natura2000", d, u)
except Exception as e:
    print("ERR n2000", e)

# BRP gewaspercelen (paged)
feats = []
start = 0
base = "https://service.pdok.nl/rvo/brpgewaspercelen/wfs/v1_0"
while True:
    d, u = wfs(base, "brpgewaspercelen:BrpGewas", hb, count=1000, start=start)
    fs = d.get("features", [])
    feats += fs
    if len(fs) < 1000:
        break
    start += 1000
save("pdok_brp", {"type": "FeatureCollection", "features": feats}, u)
