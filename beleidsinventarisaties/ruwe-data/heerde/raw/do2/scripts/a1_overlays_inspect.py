import sys, json, glob, os, collections
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/scripts')
from common import *
from shapely.validation import make_valid
gem=geom_of('heerde_gemeente.json')[0][1]
ga=gem.area
for fn in sorted(glob.glob(D+'wfs/*.json')):
    d=json.load(open(fn))
    rows=[]
    for f in d['features']:
        if not f.get('geometry'): continue
        g=make_valid(shape(f['geometry']))
        i=g.intersection(gem)
        if i.area>1:
            rows.append((f['properties'],i.area))
    tot=sum(a for _,a in rows)
    print('\n##',os.path.basename(fn),'features in bbox',len(d['features']),'intersecting',len(rows),'area ha',round(tot/1e4,1),'of gem %',round(100*tot/ga,2) if rows else 0)
    if rows:
        keys=[k for k in rows[0][0].keys() if k not in ('st_area_shape_','st_length_shape_','objectid','geo','imro','shape_area','shape_length','area','length') ]
        # print the distinct values for name-like keys
        for k in keys[:8]:
            c=collections.Counter()
            for p,a in rows: c[str(p.get(k))[:70]]+=a
            if len(c)<=12: print('   ',k,{kk:round(v/1e4,1) for kk,v in c.most_common(12)})
