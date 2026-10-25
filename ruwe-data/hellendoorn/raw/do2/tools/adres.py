# Adres -> RD-coordinaat (PDOK Locatieserver) -> verordeningsannotaties (_locationSearch). Gebruik: python3 -I adres.py "adres" ...
import sys,json,re,requests
T='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/badd7466-a102-440a-9a30-b6c10de0f032/scratchpad/hellendoorn/raw/do2/'
d=json.load(open(T+'verord_doc.json'))
for q in sys.argv[1:]:
    r=requests.get('https://api.pdok.nl/bzk/locatieserver/search/v3_1/free',params={'q':q,'rows':1,'fl':'weergavenaam,centroide_rd,type'},timeout=60).json()
    docs=r['response']['docs']
    if not docs: print(q,'niet gevonden'); continue
    x,y=re.findall(r'[\d.]+',docs[0]['centroide_rd'])
    rr=requests.get('https://ruimtelijkeplannen.overijssel.nl/api/documents/55d637e6-8ff6-4083-a824-a0e77027a044/_locationSearch',params=dict(x=x,y=y,distance=1),headers={'User-Agent':'Mozilla/5.0'},timeout=60).json()
    ids=set(rr['result']['ids']); names=set()
    for aid,an in d['annotaties'].items():
        g=set((an.get('geometry') or {}).get('ids') or [])
        if (aid in ids or g&ids) and an.get('type')=='gebiedsaanwijzing': names.add(an['name'])
    sel=sorted(n for n in names if any(k in n for k in ('andbouwgebied','NNN','bebouwd','kernrand','dorp','grondwater','intrek','essen','hoeven','landgoed','beekdal','Beekdal','veenkol','ontginning')))
    print(f"{q} -> {docs[0]['weergavenaam']} ({float(x):.0f},{float(y):.0f}): {sel}")
