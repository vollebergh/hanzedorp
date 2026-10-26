# DO2 Elburg: haalt PDOK-lagen gepagineerd op (WFS 2.0, JSON, RD) binnen bbox rond Elburg
import json, sys, urllib.request, urllib.parse, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'pdok')
BBOX = "165500,472000,181000,483000,EPSG:28992"
def fetch(base, typename, outname, page=1000, extra=""):
    feats = []; start = 0
    while True:
        q = {"service":"WFS","version":"2.0.0","request":"GetFeature","typeNames":typename,
             "outputFormat":"application/json","srsName":"EPSG:28992","bbox":BBOX,
             "count":str(page),"startIndex":str(start),"sortBy":"" }
        q.pop("sortBy")
        url = base + "?" + urllib.parse.urlencode(q)
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=180) as r:
            d = json.load(r)
        fs = d.get("features", [])
        feats += fs
        print(outname, start, len(fs), flush=True)
        if len(fs) < page: break
        start += page
    json.dump({"type":"FeatureCollection","features":feats}, open(os.path.join(OUT, outname), "w"))
    print(outname, "totaal", len(feats))
if __name__ == "__main__":
    fetch("https://service.pdok.nl/rvo/brpgewaspercelen/wfs/v1_0", "brpgewaspercelen:BrpGewas", "brp2025.json")
    fetch("https://service.pdok.nl/rvo/natura2000/wfs/v1_0", "natura2000:natura2000", "natura2000.json")
    fetch("https://service.pdok.nl/cbs/bevolkingskernen/2021/wfs/v1_0", "bevolkingskernen:bevolkingskernen", "kernen2021.json")
