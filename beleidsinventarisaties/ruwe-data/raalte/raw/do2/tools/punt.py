# Puntcontrole landbouwgebied-typologie via _locationSearch van de verordening-viewer
# Gebruik: python3 -I punt.py x y [x y ...]  (RD-coordinaten)
import sys,json,requests
T='/home/nick/.local/share/hanzedorp-raalte/raw/do2/'
d=json.load(open(T+'verord_doc.json'))
a=sys.argv[1:]
for x,y in zip(a[0::2],a[1::2]):
    r=requests.get(f'https://ruimtelijkeplannen.overijssel.nl/api/documents/55d637e6-8ff6-4083-a824-a0e77027a044/_locationSearch',params=dict(x=x,y=y,distance=1),headers={'User-Agent':'Mozilla/5.0'},timeout=60).json()
    ids=set(r['result']['ids'])
    names=set()
    for aid,an in d['annotaties'].items():
        g=set((an.get('geometry') or {}).get('ids') or [])
        if (aid in ids or g&ids) and an.get('type')=='gebiedsaanwijzing': names.add(an['name'])
    sel=[n for n in names if any(k in n for k in ('andbouwgebied','NNN','bebouwd','kernrand','Natura','grondwater','essen','landgoed','weidevogel','raat','karren'))]
    print(x,y,sorted(sel))
