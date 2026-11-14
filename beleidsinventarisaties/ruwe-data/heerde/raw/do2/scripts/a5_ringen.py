import sys, json, collections, pickle
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/scripts')
from common import *
from shapely.geometry import Point
from shapely.ops import unary_union
gem=geom_of('heerde_gemeente.json')[0][1]
L,C=pickle.load(open(D+'layers.pkl','rb'))
prod,tot=pickle.load(open(D+'agri.pkl','rb'))
kd=load('cbs_kernen.json')
K={f['properties']['naam2021']:shape(f['geometry']) for f in kd['features']}
# BAG clusters
v=json.load(open(D+'bag_vbo.json'))
ok={'Verblijfsobject in gebruik','Verblijfsobject in gebruik (niet ingemeten)','Verblijfsobject gevormd','Verbouwing verblijfsobject'}
w=[x for x in v if x['bron']=='Heerde' and 'woonfunctie' in x['doel'] and x['status'] in ok]
def cluster_poly(cx,cy,r=400,buf=45):
    pts=[Point(x['x'],x['y']) for x in w if (x['x']-cx)**2+(x['y']-cy)**2<r*r]
    return unary_union([p.buffer(buf) for p in pts]), len(pts)
extra={'Vorchten (BAG)':(203921,490269),'Hoorn (BAG/CBS-buurt)':(200930,490571),'Oenerweg-zuid (Oosterhuizen? INT)':(199443,487305),'Zwolseweg-Noord/Koerberg':(200278,491218)}
KP={}
for n in ['Heerde-Kern','Wapenveld','Veessen','Wolbert','Wapenveld-Noord','Heerde-Bakhuisbos']: KP[n]=K[n]
for n,(x,y) in extra.items():
    p,c=cluster_poly(x,y); KP[n]=p; print(n,c,round(p.area/1e4,1))
bands=[(0,250),(250,500),(500,1000),(1000,2000)]
Vrij=C['Vrij_hard']
tierA=unary_union([L['GNN'],L['N2000'],L['Weidevogel'],L['Stikstofstrook'],L['NatteLandnatuur']])
out={}
for n,kp in KP.items():
    prev=kp
    out[n]={}
    for lo,hi in bands:
        if lo==0: ring=kp.buffer(hi).difference(kp)
        else: ring=kp.buffer(hi).difference(kp.buffer(lo))
        ring=ring.intersection(gem)
        a=prod.intersection(ring)
        A=a.area
        if A<1: out[n][(lo,hi)]=(0,)*9; continue
        pc=lambda g: round(100*a.intersection(g).area/A,1)
        out[n][(lo,hi)]=(round(A/1e4,1), round(100*(A-a.intersection(Vrij).area)/A,1), pc(L['GNN']),pc(L['GOZ']),pc(L['Weidevogel']),pc(L['Ganzenrust']),pc(L['N2000']),pc(L['Stikstofstrook']),pc(L['WaardevolOpen']))
        # vrij ha
for n in out:
    print('\n##',n)
    for b,r in out[n].items():
        if r[0]==0: print(b,'geen landbouwgrond'); continue
        A=r[0]; vrijpct=100-r[1]
        print(f"{b[0]:>4}-{b[1]:<4} landbouw {A:7.1f} ha | vrij {vrijpct:5.1f}% ({A*vrijpct/100:6.1f} ha) | GNN {r[2]:5.1f} GOZ {r[3]:5.1f} weidev {r[4]:5.1f} ganzen {r[5]:5.1f} N2000 {r[6]:5.1f} N-strook {r[7]:5.1f} WOG {r[8]:5.1f}")
pickle.dump((KP,out),open(D+'ringen.pkl','wb'))
