import urllib.request, urllib.parse, re, sys, os, time
import xml.etree.ElementTree as ET
out=sys.argv[1]; q=sys.argv[2]
base="https://zoekservice.overheid.nl/sru/Search?"
start=1; rows=[]
while True:
    url=base+urllib.parse.urlencode({'x-connection':'cvdr','operation':'searchRetrieve','version':'1.2','query':q,'maximumRecords':'100','startRecord':str(start)})
    data=urllib.request.urlopen(url,timeout=120).read()
    open(os.path.join(os.path.dirname(out),'sru','cvdr_%d.xml'%start),'wb').write(data)
    root=ET.fromstring(data)
    n=int(root.find('{http://www.loc.gov/zing/srw/}numberOfRecords').text)
    recs=root.findall('.//{http://www.loc.gov/zing/srw/}record')
    for r in recs:
        def g(tag):
            el=[e for e in r.iter() if e.tag.split('}')[-1]==tag]
            return el[0].text.strip() if el and el[0].text else ''
        rows.append([g('identifier'),g('title').replace('\t',' ').replace('\n',' '),g('creator'),g('isRatifiedBy'),g('issued'),g('inwerkingtredingDatum'),g('uitwerkingtredingDatum'),g('modified'),g('isFormatOf').replace('\t',' ')])
    start+=len(recs)
    if not recs or start>n: break
with open(out,'w') as f:
    f.write('id\ttitle\tcreator\torgaan\tissued\tiwt\tuwt\tmodified\tpublicatie\n')
    for r in rows: f.write('\t'.join(r)+'\n')
print(n,len(rows))
