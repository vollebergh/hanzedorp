"""Fetch BAG panden in Hattem bbox via PDOK WFS (paged, sorted). Usage: python3 -I fetch_bag.py <outfile>"""
import json, sys, urllib.request, urllib.parse

OUT = sys.argv[1]
base = "https://service.pdok.nl/lv/bag/wfs/v2_0"
feats, start = [], 0
while True:
    p = {"service": "WFS", "request": "GetFeature", "version": "2.0.0", "typeNames": "bag:pand",
         "outputFormat": "application/json", "srsName": "EPSG:28992",
         "bbox": "196600,495300,203700,502700,EPSG:28992", "count": "1000", "startIndex": str(start),
         "sortBy": "identificatie"}
    d = json.load(urllib.request.urlopen(base + "?" + urllib.parse.urlencode(p), timeout=300))
    fs = d.get("features", [])
    feats += [{"type": "Feature", "geometry": f["geometry"],
               "properties": {k: f["properties"].get(k) for k in ("identificatie", "bouwjaar", "status", "gebruiksdoel", "aantal_verblijfsobjecten")}}
              for f in fs]
    print(start, len(fs), flush=True)
    if len(fs) < 1000:
        break
    start += 1000
json.dump({"type": "FeatureCollection", "features": feats}, open(OUT, "w"))
print("total", len(feats))
