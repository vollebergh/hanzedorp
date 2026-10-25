import json,sys
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/c389bf58-3dd2-4443-a542-c4ae17b8d9b4/scratchpad/deventer/tools/pylib2')
from shapely.geometry import shape
d=json.load(open(sys.argv[1]))
for f in d['features']:
    if f['properties']['statnaam']=='Deventer':
        g=shape(f['geometry']); print(f['properties'], g.area/1e4, g.bounds)
        json.dump(f, open('dv_gemeente.json','w'))
