"""Extra Gelderse kaartlagen (niet-verordening) voor Voorst. python3 -I fetch2.py <outdir>"""
import json, sys, os, urllib.request, urllib.parse
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
OUT=sys.argv[1]; hb=(198000,461500,211000,483000)
for ws,l in [("ngr_visie","POVI_Zoekgeb_nieuwe_natuur"),("ngr_visie","POVI_Eco_Verbindingszones"),("ngr_visie","POVI_Natte_landnatuur"),("ngr_visie","POVI_Waterberging")]:
    p={"service":"WFS","request":"GetFeature","version":"2.0.0","typeNames":f"{ws}:{l}","outputFormat":"application/json","srsName":"EPSG:28992","bbox":",".join(map(str,hb))+",EPSG:28992"}
    u=f"https://geoserver.gelderland.nl/geoserver/{ws}/wfs?"+urllib.parse.urlencode(p)
    try:
        d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=300).read())
        json.dump(d,open(os.path.join(OUT,f"{ws}_{l}.geojson"),"w"))
        open(os.path.join(OUT,"urls.txt"),"a").write(f"{ws}_{l}\t{len(d['features'])}\t{u}\n")
        print(ws,l,len(d["features"]), [ {k:v for k,v in f["properties"].items() if isinstance(v,str)} for f in d["features"][:2]])
    except Exception as e: print("ERR",l,e)
