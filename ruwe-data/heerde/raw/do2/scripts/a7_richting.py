import sys, json, pickle, math
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/scripts')
from common import *
from shapely.ops import unary_union
gem=geom_of('heerde_gemeente.json')[0][1]
L,C=pickle.load(open(D+'layers.pkl','rb'))
prod,tot=pickle.load(open(D+'agri.pkl','rb'))
KP,_=pickle.load(open(D+'ringen.pkl','rb'))
Vrij=C['Vrij_hard']
vrij=prod.difference(Vrij)
for n in ['Heerde-Kern','Wapenveld','Hoorn (BAG/CBS-buurt)','Oenerweg-zuid (Oosterhuizen? INT)','Zwolseweg-Noord/Koerberg','Wolbert']:
    kp=KP[n]; c=kp.centroid
    ring=kp.buffer(1000).difference(kp).intersection(gem)
    a=vrij.intersection(ring)
    geoms=list(a.geoms) if hasattr(a,'geoms') else [a]
    q={'N':0,'NO':0,'O':0,'ZO':0,'Z':0,'ZW':0,'W':0,'NW':0}
    names=['O','NO','N','NW','W','ZW','Z','ZO']
    for g in geoms:
        if g.is_empty or g.geom_type not in('Polygon','MultiPolygon'): continue
        cc=g.centroid; ang=math.degrees(math.atan2(cc.y-c.y,cc.x-c.x))%360
        q[names[int(((ang+22.5)%360)//45)]]+=g.area/1e4
    print(n,'vrij 0-1000 m:',round(a.area/1e4,1),'ha', {k:round(v,1) for k,v in q.items() if v>0.5})
