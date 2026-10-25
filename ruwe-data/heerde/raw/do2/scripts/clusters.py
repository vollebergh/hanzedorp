import json, collections, sys
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/scripts')
from common import *
from shapely.geometry import Point, MultiPoint
from shapely.ops import unary_union
gem=geom_of('heerde_gemeente.json')[0][1]
v=json.load(open(D+'bag_vbo.json'))
ok={'Verblijfsobject in gebruik','Verblijfsobject in gebruik (niet ingemeten)','Verblijfsobject gevormd','Verbouwing verblijfsobject'}
w=[x for x in v if x['bron']=='Heerde' and 'woonfunctie' in x['doel'] and x['status'] in ok]
print(len(w))
# cluster with 60m buffers
pts=[Point(x['x'],x['y']) for x in w]
u=unary_union([p.buffer(60) for p in pts])
comps=list(u.geoms) if u.geom_type=='MultiPolygon' else [u]
res=[]
for c in comps:
    members=[x for x,p in zip(w,pts) if c.contains(p)]
    if len(members)>=8:
        wp=collections.Counter(m['wp'] for m in members).most_common(2)
        st=collections.Counter(m['str'] for m in members).most_common(4)
        cen=c.centroid
        res.append((len(members),wp,(round(cen.x),round(cen.y)),st))
for r in sorted(res,reverse=True): print(r)
