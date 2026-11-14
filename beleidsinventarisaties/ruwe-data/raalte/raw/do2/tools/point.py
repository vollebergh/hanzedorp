import sys, json, pickle, collections
sys.path.insert(0,'/home/nick/.local/share/hanzedorp-raalte/raw/do2/tools/pylib')
from shapely import wkb
from shapely.geometry import shape, Point
from shapely.ops import unary_union
D='/home/nick/.local/share/hanzedorp-raalte/raw/do2/'
P=pickle.load(open(D+'overlay_z11.pkl','rb'))
G={g:wkb.loads(b) for g,b in P['geoms'].items()}
def byname(n):
    l=[G[g] for g in G if any(x.endswith('|'+n) for x in P['names'][g])]
    return unary_union(l) if l else None
def wfs(fn,filt=None):
    d=json.load(open(D+'wfs/'+fn))
    l=[]
    for f in d['features']:
        if not f.get('geometry'): continue
        if filt and not filt(f['properties']): continue
        g=shape(f['geometry']);
        if not g.is_valid: g=g.buffer(0)
        l.append((f['properties'],g))
    return l
layers={n:byname(n) for n in ['Landbouwgebied met generieke opgaven en kansen','Landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur','Natuurnetwerk Nederland (NNN)','bebouwd gebied','dorp of buurtschap','kernrandzone','bebouwde kom','essenlandschap','landgoed of buitenplaats','grondwaterbeschermingszone','intrekgebieden','zeer kwetsbare natuurgebieden','overstroombaar gebied','voorkeursgebieden windenergie','Beekdal en natte laagte','Leefgebied weidevogels','gesloten stortplaatsen']}
n2k=wfs('n2k_wide.json')
ess=wfs('B46_natuur_en_landschap__B46_Essen.json')
lg=wfs('B73_Cultuur__B73_Landgoederen_vlakken.json')
pts=json.loads(sys.argv[1])
for name,(x,y) in pts.items():
    p=Point(x,y)
    print('==',name,x,y)
    for n,g in layers.items():
        if g is None: print('  ',n,'(geen geometrie)'); continue
        d=g.distance(p)
        print(f'   {n}: {"IN" if d==0 else f"{d:.0f} m"}')
    best={}
    for pr,g in n2k:
        nm=pr.get('NAAM_N2K'); d=g.distance(p)
        if nm not in best or d<best[nm]: best[nm]=d
    print('   N2000:',sorted([(k,round(v)) for k,v in best.items()],key=lambda x:x[1])[:5])
    print('   Essen (WFS):', min(round(g.distance(p)) for _,g in ess))
    dl=sorted([(round(g.distance(p)),pr.get('IND_OBJ_NAAM')) for pr,g in lg])[:3]
    print('   Landgoederen (WFS):', dl)
