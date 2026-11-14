import urllib.request, urllib.parse, json
import xml.etree.ElementTree as ET
UA=open('ua.txt').read().strip()
rows=[];start=1
while True:
    q=urllib.parse.urlencode({'x-connection':'cvdr','operation':'searchRetrieve','version':'1.2','query':'dcterms.creator=Nunspeet','maximumRecords':'100','startRecord':start})
    x=urllib.request.urlopen(urllib.request.Request('https://zoekservice.overheid.nl/sru/Search?'+q,headers={'User-Agent':UA}),timeout=90).read()
    root=ET.fromstring(x)
    recs=root.findall('.//{http://www.loc.gov/zing/srw/}record')
    if not recs: break
    for rec in recs:
        d={}
        for e in rec.iter():
            t=e.tag.split('}')[1]
            if e.text and e.text.strip() and t not in('recordSchema','recordPacking','recordPosition'):
                d.setdefault(t,[]).append(e.text.strip())
        rows.append(d)
    start+=len(recs)
    if len(recs)<100: break
json.dump(rows,open('cvdr_all.json','w'),ensure_ascii=False)
print(len(rows))
