"""Afstand van gemeente Voorst (grens) tot N2000-gebieden en de stikstofstrook. python3 -I afstand_gemeente.py <geodir>"""
import json, sys, os
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely.validation import make_valid
G=sys.argv[1]
def load(name, filt=None):
    d=json.load(open(os.path.join(G,name+".geojson")))
    return unary_union([make_valid(shape(f["geometry"])) for f in d["features"] if (not filt or filt(f["properties"]))])
vo=load("kadaster_gemeentegebied_bbox",lambda p:p.get("code")=="0285")
for n in ("Veluwe","Landgoederen Brummen","Rijntakken"):
    g=load("pdok_natura2000",lambda p,n=n:p.get("naamN2K")==n); print(n,"min afstand tot gemeentegrens (m):",round(vo.distance(g)),"| overlap ha",round(vo.intersection(g).area/1e4,1))
st=load("ngr_d_Pvbb_Stikstofemissie_beperkingengebied"); print("stikstofstrook (voorbescherming): afstand tot gemeente (m):",round(vo.distance(st)),"overlap ha",round(vo.intersection(st).area/1e4,2))
