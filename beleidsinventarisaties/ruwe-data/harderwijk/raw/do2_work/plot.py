import json, sys
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from shapely.geometry import shape
from shapely.ops import unary_union
D='data/'
G=shape(json.load(open(D+'ermelo_gemeente_gm.json'))['features'][0]['geometry'])
fig,ax=plt.subplots(figsize=(11,8))
def draw(g,**kw):
    gs=[g] if g.geom_type=='Polygon' else list(getattr(g,'geoms',[]))
    first=True
    for p in gs:
        if p.geom_type=='MultiPolygon':
            sub=list(p.geoms)
        elif p.geom_type=='Polygon': sub=[p]
        else: continue
        for q in sub:
            x,y=q.exterior.xy; ax.fill(x,y,**kw); kw.pop('label',None)
def L(fn): return unary_union([shape(f['geometry']).buffer(0) for f in json.load(open(fn))['features']]).intersection(G)
draw(L(D+'pdok/natura2000.json'),color='#9ecae1',alpha=.6,label='Natura 2000')
draw(L(D+'wfs/Gelders_natuurnetwerk.json'),color='#31a354',alpha=.35,label='GNN')
draw(L(D+'wfs/Groene_ontwikkelingszone.json'),color='#fdae6b',alpha=.5,label='GOZ')
brp=[shape(f['geometry']).buffer(0) for f in json.load(open(D+'pdok/brp2025.json'))['features'] if f['properties']['category'] in ('Grasland','Bouwland','Braakland')]
draw(unary_union(brp).intersection(G),color='#ffff99',alpha=.9,label='agrarisch (BRP)')
new=shape(json.load(open(D+'wfs/Stikstofreductiegebied_alles.json'))['features'][0]['geometry'])
x,y=new.exterior.xy; ax.plot(x,y,'r-',lw=1,label='stikstofreductiegebied (rand)')
for i in new.interiors:
    x,y=i.xy; ax.plot(x,y,'r--',lw=1.2)
x,y=G.exterior.xy if G.geom_type=='Polygon' else list(G.geoms)[0].exterior.xy
ax.plot(x,y,'k-',lw=1)
ax.set_xlim(165500,181000); ax.set_ylim(472000,483000); ax.set_aspect('equal'); ax.legend(loc='lower left',fontsize=8)
plt.savefig('map.png',dpi=90)
