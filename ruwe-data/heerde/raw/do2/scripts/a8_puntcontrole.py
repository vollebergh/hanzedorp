import sys, json, pickle, re, urllib.request, urllib.parse
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/scripts')
from common import *
from shapely.geometry import Point
from shapely import wkt
L,C=pickle.load(open(D+'layers.pkl','rb'))
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
def geo(q):
    u='https://api.pdok.nl/bzk/locatieserver/search/v3_1/free?'+urllib.parse.urlencode({'q':q,'rows':1,'fq':'gemeentecode:0246'})
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60))
    if not d['response']['docs']: return None
    x=d['response']['docs'][0]
    return x['weergavenaam'], wkt.loads(x['centroide_rd'])
targets={
 'Oenerweg 38, Heerde (TAM Erve Van Lohuizen; 3 wooneenheden)':'Oenerweg 38 Heerde',
 'Zijmarseweg 5, Veessen (ontwerp-TAM, 4 woningen, rood-voor-rood)':'Zijmarseweg 5 Veessen',
 'Wapenvelder Kerkweg 24B, Wapenveld (TAM 30-06-2025, 6 woningen)':'Wapenvelder Kerkweg 24B Wapenveld',
 'Horsthoekerenk (kruising Haneweg/Eperweg; sleutelproject 500-700 wo.)':'Haneweg Heerde',
 'Horsthoekerenk (Schoolweg)':'Schoolweg Heerde',
 'Monnikenveld (Werverweg Wapenveld)':'Werverweg Wapenveld',
 'Gulbroek (natuurontwikkeling)':'Gulbroek Heerde',
 'Hoenwaard':'Hoenwaard',
 'Kerkweg 17 Vorchten':'Kerkweg 17 Vorchten',
 'Kerkweg 8 Vorchten':'Kerkweg 8 Vorchten',
 'Oenerweg 2 Heerde':'Oenerweg 2 Heerde',
 'Kavelweg 4 Heerde':'Kavelweg 4 Heerde',
 'Parallelweg 8 Wapenveld':'Parallelweg 8 Wapenveld',
}
names=['GNN','GOZ','N2000','Weidevogel','Ganzenrust','NatteLandnatuur','Stikstofstrook','NL_Veluwe','WaardevolOpen','Molenbiotoop','Intrekgebied','Streek_IJsselvallei','Streek_Veluwe','Stiltegebied','Ammoniakbuffer','ZoekgebiedNieuweNatuur','EVZ']
for t,q in targets.items():
    r=geo(q)
    if not r: print(t,'-> niet gevonden'); continue
    wn,p=r
    hits=[n for n in names if L[n].distance(p)<1]
    near=[f"{n}({round(L[n].distance(p))}m)" for n in names if 1<=L[n].distance(p)<=100]
    print(f"{t} | {wn} | RD {round(p.x)},{round(p.y)} | IN: {', '.join(hits)} | <100m: {', '.join(near)}")
