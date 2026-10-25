# Planmonitor Wonen (WFS B82_Harde_en_zachte_woningbouwplannen_vlakken) voor gemeente Raalte, met typologie per plan
import sys,json,pickle,collections
T='/home/nick/.local/share/hanzedorp-raalte/raw/do2/'
sys.path.insert(0,T+'tools/pylib')
from shapely import wkb
from shapely.geometry import shape
from shapely.ops import unary_union
P=pickle.load(open(T+'overlay_z11.pkl','rb'))
G={g:wkb.loads(b) for g,b in P['geoms'].items()}
def byname(n):
    return unary_union([G[g] for g in G if any(x.endswith('|'+n) for x in P['names'][g])])
L={'generiek':byname('Landbouwgebied met generieke opgaven en kansen'),'gebiedsspec':byname('Landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur'),'bebouwd':byname('bebouwd gebied'),'kernrandzone':byname('kernrandzone')}
d=json.load(open(T+'wfs/B82_volkshuisvesting__B82_Harde_en_zachte_woningbouwplannen_vlakken.json'))
rows=[];tot=collections.Counter();bytype=collections.Counter()
for f in d['features']:
    p=f['properties']
    if p.get('GEMEENTE')!='Raalte': continue
    g=shape(f['geometry']); g=g if g.is_valid else g.buffer(0); A=g.area
    loc={k:round(g.intersection(v).area/A*100) for k,v in L.items()}
    dom=max(['generiek','gebiedsspec','bebouwd'],key=lambda k:loc[k])
    n=p.get('NOG_TE_BOUWEN_VANAF_2026') or 0
    tot[p['STATUS_PLANOLOGISCH']]+=n; bytype[(dom,p['STATUS_PLANOLOGISCH'])]+=n
    rows.append((p['WOONPLAATS'],p['PLANNAAM'],p['STATUS_PLANOLOGISCH'],p['PLANTYPE'],n,p['JAAR_EERSTE_OPLEVERING'],p['JAAR_LAATSTE_OPLEVERING'],round(A/1e4,2),loc))
for r in sorted(rows): print(' | '.join(str(x) for x in r))
print('plannen',len(rows),'totaal',sum(tot.values()),dict(tot))
print('per dominante ligging/status',dict(bytype))
print('keys',list(d['features'][0]['properties'].keys()))
