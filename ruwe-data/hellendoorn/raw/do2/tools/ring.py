# Typologie art. 4.123 (Hellendoorn) in ringen (250/500/1000 m) rond de bebouwde kernen van Hellendoorn (verordening-viewer z11 + BRP 2025).
# Kernen = delen van annotatie 'bebouwd gebied' (> 1 ha), toegewezen aan de BAG-woonplaats waarin het zwaartepunt ligt.
# Gebruik: python3 -I ring.py -> ring.txt
import sys, json, pickle, collections
T='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/badd7466-a102-440a-9a30-b6c10de0f032/scratchpad/hellendoorn/raw/do2/'
sys.path.insert(0,T+'tools/pylib')
from shapely import wkb
from shapely.geometry import shape, Point
from shapely.ops import unary_union
gem=shape(json.load(open(T+'gemeente.json'))['geometry'])
P=pickle.load(open(T+'overlay_z11.pkl','rb'))
G={g:wkb.loads(b) for g,b in P['geoms'].items()}
def byname(n):
    l=[G[g] for g in G if any(x.endswith('|'+n) for x in P['names'][g])]
    return unary_union(l) if l else None
gen=byname('Landbouwgebied met generieke opgaven en kansen')
geb=byname('Landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur')
nnn=byname('Natuurnetwerk Nederland (NNN)'); beb=byname('bebouwd gebied'); kr=byname('kernrandzone')
ag=wkb.loads(pickle.load(open(T+'ag.pkl','rb'))['ag'])
wp={}
for f in json.load(open(T+'bag_woonplaatsen.json'))['features']:
    g=shape(f['geometry']); g=g if g.is_valid else g.buffer(0)
    if g.intersection(gem).area>0.5*g.area: wp[f['properties']['woonplaats']]=g
# Hellendoorn-variant: bebouwd gebied wordt per BAG-woonplaats geknipt (Nijverdal en Hellendoorn-dorp hangen in de verordening aan elkaar)
groups=collections.defaultdict(list)
for k,g in wp.items():
    x=beb.intersection(g)
    for p in (x.geoms if hasattr(x,'geoms') else [x]):
        if p.geom_type=='Polygon' and p.area>1e4: groups[k].append(p)
print('Bebouwd gebied (>1 ha) per BAG-woonplaats:')
for k,l in sorted(groups.items(),key=lambda kv:-sum(p.area for p in kv[1])): print(f'  {k}: {len(l)} delen, {sum(p.area for p in l)/1e4:.1f} ha')
print('Woonplaatsen zonder bebouwd-gebiedsdeel > 1 ha:',sorted(set(wp)-set(groups)))
def stat(zone):
    za=zone.area/1e4
    if za<=0: return None
    out={'zone_ha':round(za,1),'landbouwgrond_ha':round(zone.intersection(ag).area/1e4,1)}
    for nm,g in [('generiek',gen),('gebiedsspec',geb),('NNN',nnn),('kernrandzone',kr)]:
        out[nm+'_%']=round(zone.intersection(g).area/1e4/za*100,1)
    return out
print('\nRingen rond bebouwd gebied (ring minus bebouwd gebied, binnen gemeente):')
for k in sorted(groups,key=lambda k:-sum(p.area for p in groups[k])):
    u=unary_union(groups[k])
    for r in (250,500,1000):
        print(f'  {k} ring {r} m', stat(u.buffer(r).difference(beb).intersection(gem)))
print('\nTypologie per BAG-woonplaatsgebied (hele woonplaats-polygoon binnen gemeente):')
for k,g in sorted(wp.items()):
    print(f'  {k}', stat(g.intersection(gem)))
for nm,g in [('generiek',gen),('gebiedsspecifiek',geb)]:
    ps=sorted((g.geoms if hasattr(g,'geoms') else [g]),key=lambda p:-p.area)
    print('\n'+nm,'delen >100 ha:')
    for p in ps:
        if p.area<1e6: break
        c=p.representative_point(); k=[n for n,w in wp.items() if w.intersects(p)]
        big=sorted(k,key=lambda n:-wp[n].intersection(p).area)[:5]
        print(f'   {p.area/1e4:8.1f} ha; grootste overlap met woonplaatsen {big}; bounds {[round(v) for v in p.bounds]}')
