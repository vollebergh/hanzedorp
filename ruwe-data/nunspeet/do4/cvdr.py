import urllib.request, urllib.parse, re, json, sys
import xml.etree.ElementTree as ET
UA=open('ua.txt').read().strip()
ns={'d':'http://purl.org/dc/terms/','o':'http://standaarden.overheid.nl/owms/terms/','s':'http://standaarden.overheid.nl/sru','c':'http://standaarden.overheid.nl/cvdr/terms/'}
rows=[];start=1
while True:
    q=urllib.parse.urlencode({'x-connection':'cvdr','operation':'searchRetrieve','version':'1.2','query':'dcterms.creator=Nunspeet','maximumRecords':'100','startRecord':start})
    r=urllib.request.Request('https://zoekservice.overheid.nl/sru/Search?'+q,headers={'User-Agent':UA})
    x=urllib.request.urlopen(r,timeout=90).read()
    root=ET.fromstring(x)
    recs=root.findall('.//{http://www.loc.gov/zing/srw/}record')
    if not recs: break
    for rec in recs:
        g=lambda p: [e.text for e in rec.iter('{http://purl.org/dc/terms/}'+p)]
        kern={}
        for tag in ['identifier','title','creator','type','modified','issued','available','subject']:
            kern[tag]=g(tag)
        # extra fields
        extra={}
        for e in rec.iter():
            t=e.tag.split('}')[1]
            if t in('inwerkingtreding','uitwerkingtreding','datumInwerkingtreding','datumUitwerkingtreding','afkondiging','organisatietype','rechtsgebied','onderwerp','rubriek','publicatieurl','officieleTitel','citeertitel','alternative','vastgesteld','geldigheidsdatum'):
                extra.setdefault(t,[]).append((e.text or '')+str(e.attrib) if not e.text else e.text)
        rows.append({**kern,**extra})
    start+=len(recs)
    if len(recs)<100: break
json.dump(rows,open('cvdr_all.json','w'),ensure_ascii=False,indent=0)
print(len(rows))
