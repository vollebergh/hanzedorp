# DO2 Ermelo: puntentoets - in welke provinciale overlays liggen concrete Ermelose locaties (PDOK Locatieserver, RD)
import json, os, urllib.request, urllib.parse
from shapely.geometry import shape, Point
D='data'; W=D+'/wfs'
def ls(q):
    u='https://api.pdok.nl/bzk/locatieserver/search/v3_1/free?'+urllib.parse.urlencode({'q':q,'fq':'gemeentenaam:Ermelo','rows':1,'fl':'weergavenaam,type,centroide_rd'})
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))['response']['docs']
    if not d: return None
    x=d[0]; c=x['centroide_rd'].replace('POINT(','').replace(')','').split()
    return x['weergavenaam'],x['type'],float(c[0]),float(c[1])
LAYERS={'GNN':'Gelders_natuurnetwerk','GOZ':'Groene_ontwikkelingszone','Stikstofreductiegebied':'Stikstofreductiegebied','NatLandschap':'Nationale_landschappen',
        'Molenbiotoop':'Molenbiotoop','Intrekgebied':'Intrekgebieden','Natte landnatuur':'Beschzones_nat_landnat','Ammoniakbuffer':'Ammoniakbuffergebied','Provweg-zorgplicht':'Provinciale_weg_zorgplichtgebied'}
geo={k:[shape(f['geometry']).buffer(0) for f in json.load(open(os.path.join(W,fn+'.json')))['features']] for k,fn in LAYERS.items()}
geo['Natura2000']=[shape(f['geometry']).buffer(0) for f in json.load(open(D+'/pdok/natura2000.json'))['features']]
strk=[(f['properties']['streekgebied_naam'],shape(f['geometry']).buffer(0)) for f in json.load(open(W+'/Streekgebieden.json'))['features']]
Q=['Haspel 99','Haspel 123','Haspel 129','Tonnenberg 8','De Beek 77','Looweg 2','Buitenbrinkweg 41','Nijkerkerweg 54','Riebroekseweg 49','Riebroekseweg 35','Meeboerserf 6']
out=[]
for q in Q:
    try: r=ls(q)
    except Exception as e: r=None
    if not r: print(q,'-> niet gevonden'); continue
    name,typ,x,y=r; p=Point(x,y)
    hits=[k for k,gs in geo.items() if any(g.contains(p) for g in gs)]
    st=[n for n,g in strk if g.contains(p)]
    out.append({'zoekterm':q,'gevonden':name,'type':typ,'rd':[x,y],'overlays':hits,'streek':st})
    print('%-30s | %-46s | %-9s | %.0f,%.0f | streek %s | %s'%(q,name[:46],typ,x,y,','.join(st) or '-',', '.join(hits) or '(geen)'))
json.dump(out,open(D+'/puntentoets_locaties.json','w'),indent=1,ensure_ascii=False)
