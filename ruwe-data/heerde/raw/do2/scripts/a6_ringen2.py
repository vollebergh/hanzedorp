import sys, json, pickle
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/scripts')
from common import *
from shapely.ops import unary_union
gem=geom_of('heerde_gemeente.json')[0][1]
L,C=pickle.load(open(D+'layers.pkl','rb'))
prod,tot=pickle.load(open(D+'agri.pkl','rb'))
KP,_=pickle.load(open(D+'ringen.pkl','rb'))
Vrij=C['Vrij_hard']   # GNN GOZ N2000 weidevogel ganzenrust stikstof nat landnatuur
Zwaar=unary_union([L['GNN'],L['N2000'],L['Weidevogel'],L['Stikstofstrook'],L['NatteLandnatuur']])
ZwaarGOZ=unary_union([Zwaar,L['GOZ']])
bands=[(0,250),(250,500),(500,1000),(1000,2000)]
res={}
print("kern | ring | landbouw ha | vrij van alle 7 overlays (ha, %) | vrij van zware (GNN,N2000,weidevogel,stikstof,natte landnatuur) (ha,%) | vrij van zware+GOZ (ha,%) | ganzenrust % | GOZ %")
for n,kp in KP.items():
    for lo,hi in bands:
        ring=(kp.buffer(hi).difference(kp) if lo==0 else kp.buffer(hi).difference(kp.buffer(lo))).intersection(gem)
        a=prod.intersection(ring); A=a.area
        if A<1e4*0.5: continue
        v1=A-a.intersection(Vrij).area; v2=A-a.intersection(Zwaar).area; v3=A-a.intersection(ZwaarGOZ).area
        g=a.intersection(L['Ganzenrust']).area; goz=a.intersection(L['GOZ']).area
        res[f'{n}|{lo}-{hi}']=[A/1e4,v1/1e4,v2/1e4,v3/1e4,g/1e4,goz/1e4]
        print(f"{n} | {lo}-{hi} | {A/1e4:.1f} | {v1/1e4:.1f} ({100*v1/A:.0f}%) | {v2/1e4:.1f} ({100*v2/A:.0f}%) | {v3/1e4:.1f} ({100*v3/A:.0f}%) | {100*g/A:.0f}% | {100*goz/A:.0f}%")
json.dump(res,open(D+'ringen_table.json','w'),indent=1)
# totals: gemeente
A=prod.area
for nm,g in [('alle7',Vrij),('zwaar',Zwaar),('zwaar+GOZ',ZwaarGOZ)]:
    print(nm,'vrij ha',round((A-prod.intersection(g).area)/1e4,1),'%',round(100*(A-prod.intersection(g).area)/A,1))
