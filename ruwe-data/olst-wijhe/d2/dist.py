import json
from wfs import get
pts=json.load(open('pts_geo.json'))
layers={'NNN':'B46_natuur_en_landschap:B46_Natuurnetwerk_Nederland','Natura2000':'B46_natuur_en_landschap:B4_Natura_2000-gebieden','Grondwaterbeschermingsgebied':'B34_beheer_grondwater:B3_Grondwaterbeschermingsgebieden','Waterwingebied':'B34_beheer_grondwater:B3_Waterwingebieden','Nationaal Landschap':'B46_natuur_en_landschap:B4_Nationale_landschappen'}
steps=[1,100,250,500,1000,2000,3000,5000,10000]
out={}
for name,wn,x,y in pts:
    if x is None or wn=='Gemeente Olst-Wijhe': continue
    row={}
    for ln,l in layers.items():
        res=None
        for d in steps:
            try:
                r,u=get(l,f"DWITHIN(SHAPE,POINT({x} {y}),{d},meters)",count=3)
            except Exception as e:
                res=('fout',str(e)[:60]);break
            if r['features']:
                p=r['features'][0]['properties']
                nm=p.get('NAAM') or p.get('NNN_DEELGEBIED') or p.get('NATUURNETWERKNEDERLAND') or ''
                if ln=='NNN': nm=f"{p.get('NNN_DEELGEBIED')}; {p.get('LEGENDA_NNN')}"
                if ln=='Natura2000': nm=p.get('NAAM_N2K') or p.get('NAAM') or str({k:v for k,v in p.items() if 'NAAM' in k.upper()})
                res=(d,nm);break
        row[ln]=res if res else ('>10000',None)
    out[name]={'adres':wn,'x':x,'y':y,**row}
    print(name,'|',wn,'|',row,flush=True)
json.dump(out,open('dist_out.json','w'),ensure_ascii=False,indent=1)
