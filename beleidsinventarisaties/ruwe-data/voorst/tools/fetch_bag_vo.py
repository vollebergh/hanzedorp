"""BAG-verblijfsobjecten (woonfunctie, in gebruik) in gemeente Voorst via PDOK WFS (bbox-pagina's + filter op gemeentegrens).
python3 -I fetch_bag_vo.py <geodir>"""
import json, sys, urllib.request, urllib.parse, os
from shapely.geometry import shape, Point
from shapely.prepared import prep
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
G=sys.argv[1]
kad=json.load(open(os.path.join(G,"kadaster_gemeentegebied_bbox.geojson")))
vo=[shape(f["geometry"]) for f in kad["features"] if f["properties"].get("code")=="0285"][0]
pv=prep(vo); x0,y0,x1,y1=vo.bounds
base="https://service.pdok.nl/lv/bag/wfs/v2_0"
feats={}; 
# tegels van 4 km
xs=range(int(x0)//1000*1000,int(x1)+1000,4000); ys=range(int(y0)//1000*1000,int(y1)+1000,4000)
for x in xs:
    for y in ys:
        bb=(x,y,x+4000,y+4000)
        if not vo.intersects(__import__("shapely.geometry",fromlist=["box"]).box(*bb)): continue
        start=0
        while True:
            p={"service":"WFS","request":"GetFeature","version":"2.0.0","typeNames":"bag:verblijfsobject","outputFormat":"application/json","srsName":"EPSG:28992",
               "count":"1000","startIndex":str(start),"sortBy":"identificatie","bbox":",".join(map(str,bb))+",EPSG:28992"}
            d=json.loads(urllib.request.urlopen(urllib.request.Request(base+"?"+urllib.parse.urlencode(p),headers={"User-Agent":UA}),timeout=300).read())
            fs=d.get("features",[])
            for f in fs:
                pr=f["properties"]
                if "woonfunctie" in (pr.get("gebruiksdoel") or "") and pr.get("status")=="Verblijfsobject in gebruik":
                    c=f["geometry"]["coordinates"]
                    if pv.contains(Point(c[0],c[1])): feats[pr["identificatie"]]=f
            if len(fs)<1000: break
            start+=1000
        print(bb,len(feats),flush=True)
json.dump({"type":"FeatureCollection","features":list(feats.values())},open(os.path.join(G,"bag_woningen_voorst.geojson"),"w"))
print("total",len(feats))
