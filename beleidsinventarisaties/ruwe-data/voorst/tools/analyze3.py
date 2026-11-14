import json, sys, os
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely.validation import make_valid
from shapely.prepared import prep
G=sys.argv[1]
def load(name, filt=None):
    d=json.load(open(os.path.join(G,name+".geojson")))
    gs=[make_valid(shape(f["geometry"])) for f in d["features"] if f.get("geometry")]
    return unary_union(gs) if gs else None
vo=load("kadaster_gemeentegebied_bbox") if False else None
d=json.load(open(os.path.join(G,"kadaster_gemeentegebied_bbox.geojson")))
vo=unary_union([make_valid(shape(f["geometry"])) for f in d["features"] if f["properties"].get("code")=="0285"]); pv=prep(vo)
brp=json.load(open(os.path.join(G,"pdok_brp.geojson")))
ag=unary_union([make_valid(shape(f["geometry"])).intersection(vo) for f in brp["features"] if f["properties"].get("category") not in ("Natuurterrein","Landschapselement") and pv.intersects(make_valid(shape(f["geometry"])))])
for n in ("ngr_visie_POVI_Zoekgeb_nieuwe_natuur","ngr_visie_POVI_Eco_Verbindingszones","ngr_visie_POVI_Natte_landnatuur","ngr_visie_POVI_Waterberging"):
    g=load(n)
    if g is None: print(n,"leeg"); continue
    gm=g.intersection(vo).area/1e4; ga=g.intersection(ag).area/1e4
    print("| %s | %.1f | %.1f | %.1f | %.1f |"%(n,gm,100*gm/(vo.area/1e4),ga,100*ga/(ag.area/1e4)))
