import sys, json, collections
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/scripts')
from common import *
from shapely.validation import make_valid
gem=geom_of('heerde_gemeente.json')[0][1]
d=load('brp25_heerde_bbox.json')
cat=collections.Counter(); gew=collections.defaultdict(collections.Counter)
n=0
for f in d['features']:
    g=make_valid(shape(f['geometry']))
    if not g.intersects(gem): continue
    a=g.intersection(gem).area
    p=f['properties']
    cat[p['category']]+=a; gew[p['category']][p['gewas']]+=a; n+=1
print(n)
for k,v in cat.most_common(): print(k, round(v/1e4,1))
for k in gew:
    print('\n',k, [(g,round(a/1e4,1)) for g,a in gew[k].most_common(8)])
