import json,pickle,os,collections
from shapely import wkb
from shapely.geometry import shape, Point
from shapely.ops import unary_union
os.chdir('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/34361c4d-784d-4fc5-9800-df53eb03a520/scratchpad/zwartewaterland/raw')
gem=shape(json.load(open('zw_gemeente.json'))['geometry'])
P=pickle.load(open('../overlay_geoms_z12.pkl','rb'))
G={g:wkb.loads(b) for g,b in P['geoms'].items()}
def byname(n): return unary_union([G[g] for g in G if n in P['names'][g]])
gen=byname('Landbouwgebied met generieke opgaven en kansen')
geb=byname('Landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur')
nnn=byname('Natuurnetwerk Nederland (NNN)')
bebouwd=byname('bebouwd gebied')
kernrand=byname('kernrandzone')
d=json.load(open('wfs/B46_natuur_en_landschap__B4_Natura_2000-gebieden.json'))
n2k=unary_union([shape(f['geometry']).buffer(0) for f in d['features']]).intersection(gem)
ag=wkb.loads(pickle.load(open('../ag.pkl','rb'))['ag'])
kernen={'Genemuiden':(198070,513908),'Hasselt':(203711,510529),'Mastenbroek':(199618,510235),'Zwartsluis':(201635,517057)}
parts=list(bebouwd.geoms) if hasattr(bebouwd,'geoms') else [bebouwd]
parts=[p for p in parts if p.area/1e4>3]
print('bebouwd-delen >3ha:',len(parts))
assign=collections.defaultdict(list)
for p in parts:
    c=p.centroid
    k=min(kernen,key=lambda n:Point(kernen[n]).distance(c))
    assign[k].append((p, round(p.area/1e4,1), round(Point(kernen[k]).distance(c))))
for k,l in assign.items():
    print(k,[ (a,dist) for _,a,dist in sorted(l,key=lambda x:-x[1])[:6]])
def stat(zone,label):
    za=zone.area/1e4
    if za<0.01: print(label,'leeg'); return
    z_ag=zone.intersection(ag).area/1e4
    out={'zone_ha':round(za,1),'landbouwgrond_ha':round(z_ag,1)}
    for nm,g in [('generiek',gen),('gebiedsspec',geb),('NNN',nnn),('N2000',n2k),('kernrandzone',kernrand)]:
        out[nm+'_%']=round(zone.intersection(g).area/1e4/za*100,1)
    print(label,out)
for k,l in assign.items():
    u=unary_union([p for p,_,_ in l])
    ring=u.buffer(500).difference(u).intersection(gem)
    stat(ring,f'{k} ring 500m')
    ring=u.buffer(250).difference(u).intersection(gem)
    stat(ring,f'{k} ring 250m')
buiten=gem.difference(bebouwd)
stat(buiten,'buitengebied (gemeente minus bebouwd gebied)')
stat(gem,'gemeente')
