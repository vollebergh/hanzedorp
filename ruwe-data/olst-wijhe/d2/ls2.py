import json,urllib.request,sys
docs={'verordening':('55d637e6-8ff6-4083-a824-a0e77027a044','ov_2610.json'),'visie':('ffe232e7-66a3-4286-a8ef-7d73d8a7d131','visie_2610.json')}
pts=json.load(open('pts_geo.json'))
fix={'Den Nul':('Den Nul (buurt-centroide)','Buitengebied Den Nul',204464,486245),'Kleistraat Olst':('Kleistraat Olst','Kleistraat',205669,483665)}
res={}
KEY=['Landbouwgebied','Natuurnetwerk','NNN','Natura','grondwaterbeschermingszone','kernrandzone','dorp of buurtschap','bebouwd gebied','bebouwde kom','Bebouwd gebied','Kern aan','overstroombaar','boringsvrije','weidevogel','Dagelijks Stedelijk','Salland','IJssel, Vecht','Dekzand','zandgrond','rivierengebied','Rivierenlandschap','Uiterwaarden','landgoed','Landgoed','maten-','oude hoeve','Beekdal','jonge heide','essen','donkerte','bakens','Lierder','grasland','Zandgrond','Effectgebied','Verstedelijking','Natuurinclusieve','groenblauw','Grutto','Basiskwaliteit']
for dn,(eid,fn) in docs.items():
    A=json.load(open(fn))['annotaties']
    for name,wn,x,y in pts:
        if x is None or wn=='Gemeente Olst-Wijhe':
            continue
        u=f"https://ruimtelijkeplannen.overijssel.nl/api/documents/{eid}/_locationSearch?x={x}&y={y}&distance=1"
        r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60))
        s=set()
        for i in r['result']['ids']:
            a=A.get(i)
            if a and a.get('type')=='gebiedsaanwijzing' and a.get('renvooi')!='remove': s.add(a['name'])
        res.setdefault(name,{'adres':wn,'x':x,'y':y,'url':{}})
        res[name][dn]=sorted(s); res[name]['url'][dn]=u
json.dump(res,open('ls2_out.json','w'),ensure_ascii=False,indent=1)
for n,v in res.items():
    print('##',n,'|',v['adres'],'| RD',v['x'],v['y'])
    for dn in ('verordening','visie'):
        ks=[k for k in v[dn] if any(w in k for w in KEY)]
        print('  ',dn,':',' ; '.join(ks))
