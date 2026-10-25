import json, sys
from shapely.geometry import shape, box
from shapely.ops import unary_union
D='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/'
def load(fn):
    d=json.load(open(D+fn))
    return d
def geom_of(fn):
    d=load(fn)
    return [ (f.get('properties',{}), shape(f['geometry'])) for f in d['features'] if f.get('geometry')]
