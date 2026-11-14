# Typologie in ringen (250/500/1000 m) rond de bebouwde kernen van Raalte (verordening-viewer z11 + BRP 2025)
# Kernen = delen van annotatie 'bebouwd gebied' (> 1 ha) toegewezen aan de dichtstbijzijnde PDOK-woonplaatscentroide.
import sys, json, pickle, collections
T='/home/nick/.local/share/hanzedorp-raalte/raw/do2/'
sys.path.insert(0,T+'tools/pylib')
from shapely import wkb
from shapely.geometry import shape, Point
from shapely.ops import unary_union
gem=shape(json.load(open(T+'raalte_gemeente.json'))['geometry'])
P=pickle.load(open(T+'overlay_z11.pkl','rb'))
G={g:wkb.loads(b) for g,b in P['geoms'].items()}
def byname(n):
    l=[G[g] for g in G if any(x.endswith('|'+n) for x in P['names'][g])]
    return unary_union(l) if l else None
gen=byname('Landbouwgebied met generieke opgaven en kansen')
geb=byname('Landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur')
nnn=byname('Natuurnetwerk Nederland (NNN)'); beb=byname('bebouwd gebied'); kr=byname('kernrandzone')
ag=wkb.loads(pickle.load(open(T+'ag.pkl','rb'))['ag'])
W={'Raalte':(215056,490133),'Heino':(213373,495381),'Heeten':(215862,483070),'Nieuw Heeten':(219151,481974),'Luttenberg':(221551,491324),'Mariënheem':(218620,488435),'Broekland':(211613,486761),'Lierderholthuis':(209384,494846),'Laag Zuthem':(209007,497127)}
parts=[p for p in (beb.geoms if hasattr(beb,'geoms') else [beb]) if p.area>1e4]
groups=collections.defaultdict(list)
for p in parts:
    c=p.centroid; k=min(W,key=lambda n:Point(W[n]).distance(c)); d=Point(W[k]).distance(c)
    groups[k if d<2500 else f'los ({c.x:.0f},{c.y:.0f})'].append(p)
for k,l in groups.items(): print(f'{k}: {len(l)} delen, {sum(p.area for p in l)/1e4:.1f} ha')
def stat(zone,label):
    za=zone.area/1e4; a=zone.intersection(ag).area/1e4
    out={'zone_ha':round(za,1),'landbouwgrond_ha':round(a,1)}
    for nm,g in [('generiek',gen),('gebiedsspec',geb),('NNN',nnn),('kernrandzone',kr)]:
        out[nm+'_%']=round(zone.intersection(g).area/1e4/za*100,1)
    print('  ',label,out)
for k in W:
    if k not in groups: print(k,'geen bebouwd-deel'); continue
    u=unary_union(groups[k])
    for r in (250,500,1000):
        stat(u.buffer(r).difference(beb).intersection(gem),f'{k} ring {r} m')
# generieke/gebiedsspecifieke blokken
for nm,g in [('generiek',gen),('gebiedsspecifiek',geb)]:
    ps=sorted((g.geoms if hasattr(g,'geoms') else [g]),key=lambda p:-p.area)
    print(nm,'delen >50 ha:')
    for p in ps:
        if p.area<5e5: break
        c=p.centroid; k=min(W,key=lambda n:Point(W[n]).distance(c))
        print(f'   {p.area/1e4:8.1f} ha centroid ({c.x:.0f},{c.y:.0f}) nabij {k}; bounds {[round(v) for v in p.bounds]}')
