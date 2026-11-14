"""CBS wijken/buurten 2024 voor gemeente Voorst via PDOK WFS. python3 -I fetch_buurten.py <out.geojson>"""
import json, sys, urllib.request, urllib.parse
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
base="https://service.pdok.nl/cbs/wijkenbuurten/2024/wfs/v1_0"
p={"service":"WFS","request":"GetFeature","version":"2.0.0","typeNames":"wijkenbuurten:buurten","outputFormat":"application/json","srsName":"EPSG:28992","count":"500","bbox":"198000,461500,211000,483000,EPSG:28992"}
d=json.loads(urllib.request.urlopen(urllib.request.Request(base+"?"+urllib.parse.urlencode(p),headers={"User-Agent":UA}),timeout=300).read())
d["features"]=[f for f in d["features"] if str(f["properties"].get("buurtcode","")).startswith("BU0285")]
print(len(d["features"]))
json.dump(d,open(sys.argv[1],"w"))
for f in d["features"][:60]:
    pr=f["properties"]; print(pr.get("buurtcode"),pr.get("buurtnaam"),pr.get("wijknaam"),pr.get("aantal_inwoners"),pr.get("omgevingsadressendichtheid"),pr.get("stedelijkheid_adressen_per_km2"))
