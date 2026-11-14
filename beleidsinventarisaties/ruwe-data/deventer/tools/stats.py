import sys, json, pickle, collections
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/c389bf58-3dd2-4443-a542-c4ae17b8d9b4/scratchpad/deventer/tools/pylib2')
from shapely import wkb
from shapely.geometry import shape
from shapely.ops import unary_union
D='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/c389bf58-3dd2-4443-a542-c4ae17b8d9b4/scratchpad/deventer/raw2/'
z=sys.argv[1]
gem=shape(json.load(open(D+'dv_gemeente.json'))['geometry']); GA=gem.area/1e4
P=pickle.load(open(D+f'overlay_z{z}.pkl','rb'))
G={g:wkb.loads(b) for g,b in P['geoms'].items()}
def byname(n):
    l=[G[g] for g in G if any(x.endswith('|'+n) for x in P['names'][g])]
    return unary_union(l) if l else None
gen=byname('Landbouwgebied met generieke opgaven en kansen')
geb=byname('Landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur')
nnn=byname('Natuurnetwerk Nederland (NNN)'); beb=byname('bebouwd gebied'); kr=byname('kernrandzone'); dorp=byname('dorp of buurtschap')
print('overlap gen/geb ha', gen.intersection(geb).area/1e4)
print('gen',gen.area/1e4, 'geb',geb.area/1e4)
union=unary_union([gen,geb])
rest=gem.difference(union)
print('rest ha',rest.area/1e4,' of which NNN',rest.intersection(nnn).area/1e4,' bebouwd',rest.intersection(beb).area/1e4)
print('NNN in gen',nnn.intersection(gen).area/1e4,'NNN in geb',nnn.intersection(geb).area/1e4)
print('bebouwd in landbouwgebieden', beb.intersection(union).area/1e4)
# BRP
brp=json.load(open(D+'brp.json'))
cat=collections.defaultdict(float); parts=collections.defaultdict(list)
for f in brp:
    g=shape(f['geometry']).buffer(0)
    if not g.intersects(gem): continue
    gi=g.intersection(gem)
    cat[f['properties']['category']]+=gi.area/1e4
    parts[f['properties']['category']].append(gi)
print('BRP categorieen:',{k:round(v,1) for k,v in cat.items()})
ag=unary_union(parts['Grasland']+parts['Bouwland']+parts.get('Braakland',[]))
A=ag.area/1e4
print('Landbouwgrond (Grasland+Bouwland+Braakland) ha',round(A,1), round(A/GA*100,1),'% van gemeente')
for nm,g in [('generiek',gen),('gebiedsspecifiek',geb),('NNN',nnn),('kernrandzone',kr),('bebouwd gebied',beb)]:
    a=ag.intersection(g).area/1e4
    print(f'  landbouwgrond in {nm}: {a:.1f} ha = {a/A*100:.1f}%')
a=ag.difference(union).area/1e4; print(f'  landbouwgrond buiten beide typen: {a:.1f} ha = {a/A*100:.1f}%')
# share of agrarisch buitengebied: gen+geb as denominator
U=union.area/1e4
print(f'landbouwgebied totaal (gen+geb): {U:.1f} ha = {U/GA*100:.1f}% ; generiek {gen.area/1e4/U*100:.1f}% / gebiedsspecifiek {geb.area/1e4/U*100:.1f}% daarvan')
# WFS overlays inside landbouwgebied types
def wfsu(fn):
    d=json.load(open(D+'wfs/'+fn)); l=[]
    for f in d['features']:
        if f.get('geometry'):
            g=shape(f['geometry']); g=g if g.is_valid else g.buffer(0); l.append(g)
    return unary_union(l).intersection(gem)
for lab,fn in [('Natura2000','B46_natuur_en_landschap__B4_Natura_2000-gebieden.json'),('GWB','B34_beheer_grondwater__B3_Grondwaterbeschermingsgebieden.json'),('Intrek','B34_beheer_grondwater__B3_Intrekgebieden_potentiele_waterwinning.json'),('Essen','B46_natuur_en_landschap__B46_Essen.json'),('Landgoederen','B73_Cultuur__B73_Landgoederen_vlakken.json'),('ONW','Informatiekaart_Natuur__IKN_Zone_Ondernemen_met_Natuur_en_Water.json')]:
    g=wfsu(fn)
    print(f'{lab}: gemeente {g.area/1e4:.1f} ha ({g.area/1e4/GA*100:.1f}%); in generiek {g.intersection(gen).area/1e4:.1f}; in gebiedsspec {g.intersection(geb).area/1e4:.1f}; op landbouwgrond {g.intersection(ag).area/1e4:.1f}')
pickle.dump({'ag':ag.wkb},open(D+'ag.pkl','wb'))
