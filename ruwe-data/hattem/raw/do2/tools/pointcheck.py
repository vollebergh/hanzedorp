"""Geocode street addresses (PDOK locatieserver) in Hattem and test overlays. Usage: python3 -I pointcheck.py <geodir> street1 [street2 ...]"""
import sys,json,os,urllib.request,urllib.parse
from shapely.geometry import shape, Point
from shapely.ops import unary_union
from shapely.validation import make_valid
G=sys.argv[1]
L={"GNN":"POVE_Gelders_natuurnetwerk","GOZ":"POVE_Groene_ontwikkelingszone","Weidevogel":"POVE_Weidevogelgebieden","Ganzenrust":"POVE_Ganzenrustgebieden","Stikstof":"ngr_d_Pvbb_Stikstofemissie_beperkingengebied","N2000":"pdok_natura2000","NL Veluwe":"POVE_Nationale_landschappen","Molenbiotoop":"POVE_Molenbiotoop","Boringsvrij":"POVE_Boringsvrije_zone","NatteLN":"POVE_Beschzones_nat_landnat"}
U={k:unary_union([make_valid(shape(f["geometry"])) for f in json.load(open(os.path.join(G,v+".geojson")))["features"]]) for k,v in L.items()}
st=[s for s in json.load(open(os.path.join(G,"POVE_Streekgebieden.geojson")))["features"]]
for street in sys.argv[2:]:
    q=urllib.parse.urlencode({"q":f'straatnaam:"{street}" AND woonplaatsnaam:Hattem',"fq":"type:adres","rows":100,"fl":"weergavenaam,centroide_rd"})
    d=json.load(urllib.request.urlopen("https://api.pdok.nl/bzk/locatieserver/search/v3_1/free?"+q))
    for doc in d["response"]["docs"]:
        x,y=map(float,doc["centroide_rd"][6:-1].split())
        p=Point(x,y)
        hits=[k for k,g in U.items() if g.contains(p)]
        s=[f["properties"]["streekgebied_naam"] for f in st if make_valid(shape(f["geometry"])).contains(p)]
        print(doc["weergavenaam"],round(x),round(y),hits,s)
