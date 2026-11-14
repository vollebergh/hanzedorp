import json
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely.strtree import STRtree
G='geo/'
v=json.load(open(G+'voorst.json')); gem=shape(v['geometry']).buffer(0)
A=gem.area
def load(n):
    d=json.load(open(G+n+'.json'))
    return d['features']
def geoms(fs):
    out=[]
    for f in fs:
        if f['geometry'] is None: continue
        try: out.append(shape(f['geometry']).buffer(0))
        except Exception: pass
    return out
layers={}
for L in ['POVE_Gelders_natuurnetwerk','POVE_Groene_ontwikkelingszone','POVE_Weidevogelgebieden','POVE_Ganzenrustgebieden','POVE_Beschzones_nat_landnat','POVE_Nationale_landschappen','POVE_Waterwingebieden','POVE_Intrekgebieden','POVE_Boringsvrije_zone','POVE_Molenbiotoop','POVE_Ammoniakbuffergebied','POVE_Oude_bosgroeiplaatsen','POVE_Windturbines_aandachtsgebied_rondom_de_Veluwe','stikstof','n2000']:
    fs=load(L)
    u=unary_union(geoms(fs)).intersection(gem)
    layers[L]=u
    print(L, len(fs), f'{u.area/A*100:.1f}% van gemeente ({u.area/1e4:.0f} ha)')
# streken
fs=load('POVE_Streekgebieden')
for f in fs:
    u=shape(f['geometry']).buffer(0).intersection(gem)
    print('streek',f['properties'].get('streek') or f['properties'], f'{u.area/A*100:.1f}%')
print([f['properties'] for f in load('POVE_Nationale_landschappen')][:1])
print([f['properties'] for f in load('POVE_Weidevogelgebieden')][:3])
print([ (f['properties']) for f in load('POVE_Ganzenrustgebieden')][:6])
# BRP
brp=load('brp')
import collections
cat=collections.Counter()
areas=collections.defaultdict(float)
landb=[]
for f in brp:
    g=shape(f['geometry']).buffer(0)
    gi=g.intersection(gem)
    if gi.is_empty: continue
    c=f['properties']['category']
    areas[c]+=gi.area/1e4
    if c in ('Grasland','Bouwland'):
        landb.append(gi)
print({k:round(v) for k,v in areas.items()})
lb=unary_union(landb); LA=lb.area
print('productieve landbouwgrond (grasland+bouwland) ha',LA/1e4)
res={}
for L,u in layers.items():
    if u.is_empty: print('  ',L,'leeg'); continue
    x=lb.intersection(u).area
    res[L]=x
    print(f'  {L}: {x/LA*100:.1f}% van landbouwgrond')
def comb(names):
    u=unary_union([layers[n] for n in names if not layers[n].is_empty]); return lb.intersection(u).area/LA*100
print('GNN of GOZ',comb(['POVE_Gelders_natuurnetwerk','POVE_Groene_ontwikkelingszone']))
print('GNN/GOZ/weidevogel/ganzenrust/N2000', comb(['POVE_Gelders_natuurnetwerk','POVE_Groene_ontwikkelingszone','POVE_Weidevogelgebieden','POVE_Ganzenrustgebieden','n2000']))
print('Allen incl. NL Veluwe', comb(['POVE_Gelders_natuurnetwerk','POVE_Groene_ontwikkelingszone','POVE_Weidevogelgebieden','POVE_Ganzenrustgebieden','n2000','stikstof']))
free=lb.difference(unary_union([layers[n] for n in ['POVE_Gelders_natuurnetwerk','POVE_Groene_ontwikkelingszone','POVE_Weidevogelgebieden','POVE_Ganzenrustgebieden','n2000']]))
print('landbouwgrond zonder GNN/GOZ/weidevogel/ganzenrust/N2000/stikstof ha',free.area/1e4, f'{free.area/LA*100:.1f}%')
# also without ganzenrust (ganzenrust is voorwaardelijk)
json.dump({'free_ha':free.area/1e4},open(G+'res.json','w'))
