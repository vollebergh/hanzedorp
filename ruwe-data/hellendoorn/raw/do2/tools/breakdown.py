# Oppervlak per attribuutwaarde van een (al gedownloade) WFS-laag binnen de gemeente Raalte
# Gebruik: python3 -I breakdown.py <bestandsnaam in wfs/> <attribuut>
import sys,json,collections
T='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/badd7466-a102-440a-9a30-b6c10de0f032/scratchpad/hellendoorn/raw/do2/'
sys.path.insert(0,T+'tools/pylib')
from shapely.geometry import shape
from shapely.ops import unary_union
gem=shape(json.load(open(T+'gemeente.json'))['geometry']); GA=gem.area/1e4
d=json.load(open(T+'wfs/'+sys.argv[1]))
parts=collections.defaultdict(list)
for f in d['features']:
    if not f.get('geometry'): continue
    g=shape(f['geometry']); g=g if g.is_valid else g.buffer(0)
    if not g.intersects(gem): continue
    parts[str(f['properties'].get(sys.argv[2]))].append(g.intersection(gem))
for k,l in sorted(parts.items(),key=lambda kv:-unary_union(kv[1]).area):
    a=unary_union(l).area/1e4
    print(f'{a:9.1f} ha {a/GA*100:5.1f}%  n={len(l)}  {k}')
