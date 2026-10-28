import json
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely import make_valid
D='data/'
G=shape(json.load(open(D+'harderwijk_gemeente_gm.json'))['features'][0]['geometry'])
fig,ax=plt.subplots(figsize=(12,10))
def draw(g,**kw):
    if g.is_empty: return
    gs=list(g.geoms) if hasattr(g,'geoms') else [g]
    for p in gs:
        subs=list(p.geoms) if p.geom_type=='MultiPolygon' else ([p] if p.geom_type=='Polygon' else [])
        for q in subs:
            x,y=q.exterior.xy; ax.fill(x,y,**kw); kw.pop('label',None)
def L(fn): return make_valid(unary_union([make_valid(shape(f['geometry'])) for f in json.load(open(fn))['features']])).intersection(G)
draw(L(D+'pdok/natura2000.json'),color='#9ecae1',alpha=.6,label='Natura 2000')
draw(L(D+'wfs/Gelders_natuurnetwerk.json'),color='#31a354',alpha=.35,label='GNN')
draw(L(D+'wfs/Groene_ontwikkelingszone.json'),color='#fdae6b',alpha=.6,label='GOZ')
brp=[make_valid(shape(f['geometry'])) for f in json.load(open(D+'pdok/brp2025.json'))['features'] if f['properties']['category'] in ('Grasland','Bouwland','Braakland')]
draw(unary_union(brp).intersection(G),color='#ffff00',alpha=.9,label='agrarisch (BRP)')
sr=L(D+'wfs/Stikstofreductiegebied.json')
draw(sr,color='none',edgecolor='red',alpha=1,label='stikstofreductiegebied')
for g in (list(sr.geoms) if hasattr(sr,'geoms') else [sr]):
    if g.geom_type=='Polygon':
        x,y=g.exterior.xy; ax.plot(x,y,'r-',lw=1)
for f in json.load(open(D+'pdok/kernen2021.json'))['features']:
    s=make_valid(shape(f['geometry']))
    if s.intersects(G):
        c=s.centroid; ax.text(c.x,c.y,f['properties'].get('kernnaam','?')[:12],fontsize=7)
x,y=(G.exterior.xy if G.geom_type=='Polygon' else list(G.geoms)[0].exterior.xy)
ax.plot(x,y,'k-',lw=1)
ax.set_xlim(166500,178000); ax.set_ylim(479000,488500); ax.set_aspect('equal'); ax.legend(loc='lower left',fontsize=8)
plt.savefig('map.png',dpi=80)
