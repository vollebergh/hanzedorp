import sys, json, pickle, collections
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/c389bf58-3dd2-4443-a542-c4ae17b8d9b4/scratchpad/deventer/tools/pylib2')
from shapely import wkb
from shapely.geometry import shape, Point
from shapely.ops import unary_union
D='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/c389bf58-3dd2-4443-a542-c4ae17b8d9b4/scratchpad/deventer/raw2/'
gem=shape(json.load(open(D+'dv_gemeente.json'))['geometry'])
P=pickle.load(open(D+'overlay_z11.pkl','rb'))
G={g:wkb.loads(b) for g,b in P['geoms'].items()}
def byname(n):
    l=[G[g] for g in G if any(x.endswith('|'+n) for x in P['names'][g])]
    return unary_union(l) if l else None
gen=byname('Landbouwgebied met generieke opgaven en kansen')
geb=byname('Landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur')
nnn=byname('Natuurnetwerk Nederland (NNN)'); beb=byname('bebouwd gebied'); kr=byname('kernrandzone'); dorp=byname('dorp of buurtschap')
ag=wkb.loads(pickle.load(open(D+'ag.pkl','rb'))['ag'])
kernen={'Deventer (stad)':(210006,473868),'Colmschate':(212040,473876),'Bathmen':(218812,473791),'Diepenveen':(207446,478732),'Lettele':(215704,476986),'Okkenbroek':(218328,478112),'Schalkhaar':(211591,478275)}
parts=[p for p in (beb.geoms if hasattr(beb,'geoms') else [beb]) if p.area>1e4]

def stat(zone,label):
    za=zone.area/1e4
    out={'zone_ha':round(za,1),'landbouwgrond_ha':round(zone.intersection(ag).area/1e4,1)}
    for nm,g in [('generiek',gen),('gebiedsspec',geb),('NNN',nnn),('kernrandzone',kr)]:
        out[nm+'_%']=round(zone.intersection(g).area/1e4/za*100,1)
    print(label,out)
named={'Stad (aaneengesloten)':(209072,475001),'Bathmen':(216499,473859),'Lettele':(215431,477000),'Okkenbroek':(218615,479253),'deel 117 ha zuid':(210687,471835),'deel 8.9 ha':(210729,476854),'deel 7.2 ha':(220027,474276),'deel 5.3 ha':(216441,475115)}
for k,(x,y) in named.items():
    c=[p for p in parts if p.distance(Point(x,y))<1]
    if not c: print(k,'niet gevonden'); continue
    u=c[0]
    for r in (250,500,1000):
        ring=u.buffer(r).difference(beb).intersection(gem)
        stat(ring,f'{k} ring {r} m')
