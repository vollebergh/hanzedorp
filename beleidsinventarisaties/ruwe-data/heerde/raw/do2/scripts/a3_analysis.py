import sys, json, collections, pickle
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/scripts')
from common import *
from shapely.validation import make_valid
from shapely.ops import unary_union
from shapely.prepared import prep
gem=geom_of('heerde_gemeente.json')[0][1]
GA=gem.area
def layer(fn, filt=None):
    d=load(fn); gs=[]
    for f in d['features']:
        if not f.get('geometry'): continue
        if filt and not filt(f['properties']): continue
        g=make_valid(shape(f['geometry'])).intersection(gem)
        if not g.is_empty: gs.append(g)
    return unary_union(gs) if gs else shape({'type':'GeometryCollection','geometries':[]})
L={}
L['GNN']=layer('wfs/Gelders_natuurnetwerk.json')
L['GOZ']=layer('wfs/Groene_ontwikkelingszone.json')
L['N2000']=layer('wfs/n2k.json')
L['N2000_Veluwe']=layer('wfs/n2k.json',lambda p:p['naamN2K']=='Veluwe')
L['N2000_Rijntakken']=layer('wfs/n2k.json',lambda p:p['naamN2K']=='Rijntakken')
L['Weidevogel']=layer('wfs/Weidevogelgebieden.json')
L['Ganzenrust']=layer('wfs/Ganzenrustgebieden.json')
L['NatteLandnatuur']=layer('wfs/Beschzones_nat_landnat.json')
L['Stikstofstrook']=layer('wfs/ngr_d_Pvbb_Stikstofemissie_beperkingengebied.json')
L['NL_Veluwe']=layer('wfs/Nationale_landschappen.json')
L['WaardevolOpen']=layer('wfs/ikn_Waardevolle_Open_gebieden.json')
L['Molenbiotoop']=layer('wfs/Molenbiotoop.json')
L['Intrekgebied']=layer('wfs/Intrekgebieden.json')
L['Stiltegebied']=layer('wfs/Stiltegebieden.json')
L['Streek_IJsselvallei']=layer('wfs/Streekgebieden.json',lambda p:p['streekgebied_naam']=='IJsselvallei')
L['Streek_Veluwe']=layer('wfs/Streekgebieden.json',lambda p:p['streekgebied_naam']=='Veluwe')
L['Ammoniakbuffer']=layer('wfs/Ammoniakbuffergebied.json')
L['OudeBosgroeiplaats']=layer('wfs/Oude_bosgroeiplaatsen.json')
L['ZoekgebiedNieuweNatuur']=layer('wfs/ngr_visie_POVI_Zoekgeb_nieuwe_natuur.json')
L['EVZ']=layer('wfs/ngr_visie_POVI_Eco_Verbindingszones.json')
L['Aardkundig_internationaal']=layer('wfs/ngr_a_Ab_Aardkundige_waarde.json',lambda p:'internationaal' in p['waardering'])
L['Aardkundig_nationaal']=layer('wfs/ngr_a_Ab_Aardkundige_waarde.json',lambda p:'nationaal' in p['waardering'])
L['Aardkundig_alle']=layer('wfs/ngr_a_Ab_Aardkundige_waarde.json')
L['Belvoir']=layer('wfs/ngr_a_ChAr_DN_Belvoirgebieden.json')
L['ArcheoParel']=layer('wfs/ngr_a_ChAr_DN_Parels.json')
L['Grondwaterfluctuatie']=layer('wfs/ngr_d_POPR_RWP_Grondwaterfluctuatiezone.json')
L['WindVerbod']=layer('wfs/Windturbines_verbodsgebied_Veluwe.json')
L['WindAandacht']=layer('wfs/Windturbines_aandachtsgebied_rondom_de_Veluwe.json')
L['ProvWegBeperking']=layer('wfs/Provinciale_wegen_beperking.json')
# aliases / empty
for k in ['Waterwin','GWBG','Boringsvrij','KWO','ASV','Waterlinie','Limes']:
    L[k]=shape({'type':'GeometryCollection','geometries':[]})
E=lambda *k: unary_union([L[x] for x in k])
C={}
C['GNN_of_GOZ']=E('GNN','GOZ')
C['NatuurVogel']=E('GNN','GOZ','N2000','Weidevogel','Ganzenrust')
C['NatuurVogelStikstof']=E('GNN','GOZ','N2000','Weidevogel','Ganzenrust','Stikstofstrook')
C['Vrij_hard']=E('GNN','GOZ','N2000','Weidevogel','Ganzenrust','Stikstofstrook','NatteLandnatuur')
NL_buiten=L['NL_Veluwe'].difference(E('GNN','GOZ'))
C['BOPA_advies_alles']=unary_union([E('GNN','GOZ','NatteLandnatuur','Ganzenrust','Weidevogel','WaardevolOpen','Molenbiotoop','Intrekgebied'),NL_buiten])
C['BOPA_advies_zonder_NL']=E('GNN','GOZ','NatteLandnatuur','Ganzenrust','Weidevogel','WaardevolOpen','Molenbiotoop','Intrekgebied')
C['BOPA_advies_zonder_NL_en_intrek']=E('GNN','GOZ','NatteLandnatuur','Ganzenrust','Weidevogel','WaardevolOpen','Molenbiotoop')
C['Vrij_alles_incl_WOG_molen']=E('GNN','GOZ','N2000','Weidevogel','Ganzenrust','Stikstofstrook','NatteLandnatuur','WaardevolOpen','Molenbiotoop','Intrekgebied')
pickle.dump((L,C),open(D+'layers.pkl','wb'))
print({k:round(v.area/1e4,1) for k,v in L.items()})
print({k:round(v.area/1e4,1) for k,v in C.items()})
