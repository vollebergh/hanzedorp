"""Fetch Voorst (GM0285) boundary. python3 -I bounds.py <outdir>"""
import json, sys, urllib.request, urllib.parse
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
OUT=sys.argv[1]
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=300).read()
rb=(195000,462000,215000,485000)
for name,base,tn in [("kadaster_gemeentegebied","https://service.pdok.nl/kadaster/bestuurlijkegebieden/wfs/v1_0","bestuurlijkegebieden:Gemeentegebied"),
                    ("cbs2024_gemeenten","https://service.pdok.nl/cbs/gebiedsindelingen/2024/wfs/v1_0","gebiedsindelingen:gemeente_niet_gegeneraliseerd")]:
    p={"service":"WFS","request":"GetFeature","version":"2.0.0","typeNames":tn,"outputFormat":"application/json","srsName":"EPSG:28992","bbox":",".join(map(str,rb))+",EPSG:28992"}
    u=base+"?"+urllib.parse.urlencode(p)
    d=json.loads(get(u))
    json.dump(d,open(f"{OUT}/{name}_bbox.geojson","w"))
    print(name,len(d["features"]),[ (f["properties"].get("code") or f["properties"].get("statcode"), f["properties"].get("naam") or f["properties"].get("statnaam")) for f in d["features"]])
