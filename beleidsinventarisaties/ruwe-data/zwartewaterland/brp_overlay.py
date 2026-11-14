import json,pickle,collections,sys
from shapely import wkb
from shapely.geometry import shape
from shapely.ops import unary_union
import os
os.chdir('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/34361c4d-784d-4fc5-9800-df53eb03a520/scratchpad/zwartewaterland/raw')
gem=shape(json.load(open('zw_gemeente.json'))['geometry'])
P=pickle.load(open('../overlay_geoms_z12.pkl','rb'))
G={g:wkb.loads(b) for g,b in P['geoms'].items()}
def byname(n): 
    return unary_union([G[g] for g in G if n in P['names'][g]])
gen=byname('Landbouwgebied met generieke opgaven en kansen')
geb=byname('Landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur')
nnn=byname('Natuurnetwerk Nederland (NNN)')
# natura 2000 from wfs
d=json.load(open('wfs/B46_natuur_en_landschap__B4_Natura_2000-gebieden.json'))
n2k=unary_union([shape(f['geometry']).buffer(0) for f in d['features']]).intersection(gem)
brp=json.load(open('brp.json'))
cat=collections.defaultdict(float)
agg=collections.defaultdict(float)
tot=0
parts=[]
for f in brp:
    g=shape(f['geometry']).buffer(0)
    if not g.intersects(gem): continue
    gi=g.intersection(gem)
    a=gi.area/1e4
    p=f['properties']
    cat[p['category']]+=a
    parts.append((p['category'],gi))
    tot+=a
print('BRP totaal in gemeente ha',round(tot,1))
for k,v in sorted(cat.items(), key=lambda kv:-kv[1]): print(f'  {k}: {v:.1f} ha')
# landbouwgrond = cat not in some set
nonag=('Natuurterreinen','Bossen','Overig')
ag=[gi for c,gi in parts if c not in ('Natuurterreinen',)]
agu=unary_union(ag)
print('Landbouwgrond (excl. natuurterreinen) ha', round(agu.area/1e4,1))
for name,geom in [('generiek',gen),('gebiedsspecifiek',geb),('NNN',nnn),('Natura2000',n2k)]:
    a=agu.intersection(geom).area/1e4
    print(f'  landbouwgrond in {name}: {a:.1f} ha = {a/(agu.area/1e4)*100:.1f}%')
rest=agu.difference(unary_union([gen,geb]))
print('  landbouwgrond buiten beide typen:', round(rest.area/1e4,1))
# grasland / akkerbouw
for c in ['Grasland','Bouwland','Akkerbouw','Maïs','Mais']:
    pass
pickle.dump({'ag':agu.wkb}, open('../ag.pkl','wb'))
