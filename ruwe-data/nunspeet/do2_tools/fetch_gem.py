import json, sys, urllib.request, urllib.parse
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
OUT=sys.argv[1]
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=300).read()
p={"service":"WFS","request":"GetFeature","version":"2.0.0","typeNames":"bestuurlijkegebieden:Gemeentegebied","outputFormat":"application/json","srsName":"EPSG:28992","bbox":"170000,480000,215000,520000,EPSG:28992"}
d=json.loads(get("https://service.pdok.nl/kadaster/bestuurlijkegebieden/wfs/v1_0?"+urllib.parse.urlencode(p)))
json.dump(d,open(OUT,"w"))
from shapely.geometry import shape
for f in d["features"]:
    print(f["properties"].get("code"),f["properties"].get("naam"),[round(b) for b in shape(f["geometry"]).bounds])
