import json, sys, urllib.request, urllib.parse
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
OUT=sys.argv[1]
bb="172000,473000,191000,493500,EPSG:28992"
def wfs(base,tn):
    p={"service":"WFS","request":"GetFeature","version":"2.0.0","typeNames":tn,"outputFormat":"application/json","srsName":"EPSG:28992","bbox":bb,"count":"2000"}
    return json.loads(urllib.request.urlopen(urllib.request.Request(base+"?"+urllib.parse.urlencode(p),headers={"User-Agent":UA}),timeout=300).read())
d=wfs("https://service.pdok.nl/cbs/bevolkingskernen/2021/wfs/v1_0","bevolkingskernen:bevolkingskernen")
json.dump(d,open(OUT+"/cbs_bevolkingskernen.geojson","w"))
print(len(d["features"]),[ (f["properties"]) for f in d["features"]][:3])
d=wfs("https://service.pdok.nl/lv/bag/wfs/v2_0","bag:woonplaats")
json.dump(d,open(OUT+"/bag_woonplaats.geojson","w"))
print(len(d["features"]),[f["properties"].get("naam") for f in d["features"]])
d=wfs("https://service.pdok.nl/cbs/gebiedsindelingen/2024/wfs/v1_0","gebiedsindelingen:buurt_niet_gegeneraliseerd")
json.dump(d,open(OUT+"/cbs_buurt.geojson","w"))
print(len(d["features"]),list(d["features"][0]["properties"].items())[:10])
