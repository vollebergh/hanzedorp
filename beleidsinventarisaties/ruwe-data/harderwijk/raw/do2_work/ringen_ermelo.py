# DO2 Ermelo: ringen rond kernen/buurtschappen - agrarisch gebied (BRP 2025 excl. natuurterrein/overige) en overlay-druk; namen van gebieden
# Draaien: /home/nick/.venv/bin/python3 -I ringen_ermelo.py  (vanuit deze map)
import json, os, collections
from shapely.geometry import shape, Point
from shapely.ops import unary_union
D='data'; W=D+'/wfs'
G=shape(json.load(open(D+'/ermelo_gemeente_gm.json'))['features'][0]['geometry'])
def L(fn):
    out=[]
    for f in json.load(open(fn))['features']:
        s=shape(f['geometry'])
        if not s.is_valid: s=s.buffer(0)
        if s.intersects(G): out.append((f['properties'],s))
    return out
brp=[(f['properties'],shape(f['geometry']).buffer(0)) for f in json.load(open(D+'/pdok/brp2025.json'))['features']]
agr=unary_union([s.intersection(G) for p,s in brp if p['category'] not in('Natuurterrein','Overige') and s.intersects(G)])
def lay(fn): return unary_union([s for p,s in L(os.path.join(W,fn))]).intersection(G)
OV={'GNN':lay('Gelders_natuurnetwerk.json'),'GOZ':lay('Groene_ontwikkelingszone.json'),
    'Natte landnatuur':lay('Beschzones_nat_landnat.json'),'Stikstofgebied':lay('Stikstofreductiegebied.json'),
    'Intrekgebied':lay('Intrekgebieden.json'),'Molenbiotoop':lay('Molenbiotoop.json'),'Ammoniakbuffer':lay('Ammoniakbuffergebied.json'),
    'Veluwe-streek':unary_union([s for p,s in L(W+'/Streekgebieden.json') if p['streekgebied_naam']=='Veluwe']).intersection(G),
    'Randmeerkust':unary_union([s for p,s in L(W+'/Streekgebieden.json') if p['streekgebied_naam']=='Randmeerkust']).intersection(G),
    'NL Veluwe':lay('Nationale_landschappen.json')}
n2=unary_union([s for p,s in L(D+'/pdok/natura2000.json')]).intersection(G); OV['Natura2000']=n2
VRIJ=['GNN','GOZ','Stikstofgebied','Natura2000']  # weidevogel/ganzenrust: 0 in Ermelo
vrij_u=unary_union([OV[k] for k in VRIJ])
kernen={}
for f in json.load(open(D+'/pdok/kernen2021.json'))['features']:
    s=shape(f['geometry']).buffer(0)
    if s.intersection(G).area>1e4 and f['properties']['naam2021'] in('Ermelo-Kern','Ermelo-Horst'): kernen[f['properties']['naam2021']]=s
# buurtschappen: clusters uit BAG-woonobjecten (zie clusters.py)
pts=[]
for f in json.load(open(D+'/pdok/bag_vbo.json'))['features']:
    p=f['properties']
    if 'woonfunctie' in (p.get('gebruiksdoel') or '') and p['status']=='Verblijfsobject in gebruik':
        x,y=f['geometry']['coordinates']
        if G.contains(Point(x,y)): pts.append(Point(x,y))
def cluster(cx,cy,r=400):
    c=Point(cx,cy); sel=[p for p in pts if p.distance(c)<r]
    return unary_union([p.buffer(60) for p in sel]), len(sel)
for nm,(cx,cy) in {'Speuld (cluster Garderenseweg/Buurtweg/Lageveld)':(177096,475736),'Leuvenum (Leuvenumseweg)':(173210,479404),'Staverden':(179043,477659),'Telgt (Jacobslaan/Nieuwelaan)':(171360,476576)}.items():
    g,n=cluster(cx,cy); kernen[nm]=g; print('cluster',nm,n,'woningen binnen 400 m van',cx,cy)
out=[]
for nm,k in kernen.items():
    print('\nKERN',nm,'kernoppervlak ha %.1f'%(k.area/1e4),'| in stikstofgebied %.0f%%, GNN %.0f%%, GOZ %.0f%%, N2000 %.0f%%'%tuple(k.intersection(OV[o]).area/k.area*100 for o in('Stikstofgebied','GNN','GOZ','Natura2000')))
    for lo,hi in [(0,250),(250,500),(500,1000),(1000,2000)]:
        ring=(k.buffer(hi).difference(k.buffer(lo)) if lo else k.buffer(hi).difference(k)).intersection(agr)
        if ring.is_empty or ring.area<1e3: print('  ring %d-%d m: geen agrarisch gebied'%(lo,hi)); continue
        a=ring.area/1e4; row={'kern':nm,'ring':'%d-%d'%(lo,hi),'agr_ha':round(a,1)}
        for key in OV: row[key]=round(ring.intersection(OV[key]).area/ring.area*100)
        row['vrij']=round(ring.difference(vrij_u).area/ring.area*100); out.append(row)
        print('  ring %4d-%4d m: agr %.0f ha | vrij %d%% | '%(lo,hi,a,row['vrij'])+' '.join('%s %d%%'%(k2,row[k2]) for k2 in OV if row[k2]))
json.dump(out,open(D+'/ringen_kernen.json','w'),indent=1)
def names(fn,key,extra=()):
    c=collections.defaultdict(float)
    for p,s in L(os.path.join(W,fn)):
        c[' | '.join(str(p.get(k)) for k in (key,)+tuple(extra))]+=s.intersection(G).area/1e4
    return {k:round(v,1) for k,v in sorted(c.items(),key=lambda x:-x[1]) if v>0.05}
print('\nGNN regio',names('Gelders_natuurnetwerk.json','regio'))
print('GOZ regio',names('Groene_ontwikkelingszone.json','regio'))
print('NATLANDSCHAP',names('Nationale_landschappen.json','gebiedsnaam'))
print('STREEK',names('Streekgebieden.json','streekgebied_naam',('deelgebied_naam',)))
print('INTREK',names('Intrekgebieden.json','objectnaam'))
print('MOLEN',names('Molenbiotoop.json','objectnaam'))
print('NATTE',names('Beschzones_nat_landnat.json','gebiedsnaam'))
print('WATERSCHAP',names('Waterschappen.json','waterschap'))
print('PROVWEG',names('Provinciale_wegen.json','objectnaam',('beheerder',)))
print('STILTE',names('Stiltegebieden.json','gebiedsnaam'))
print('N2000',{nm:round(sum(s.intersection(G).area for p,s in L(D+'/pdok/natura2000.json') if p['naamN2K']==nm)/1e4,1) for nm in set(p['naamN2K'] for p,s in L(D+'/pdok/natura2000.json'))})
