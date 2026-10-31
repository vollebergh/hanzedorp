import urllib.request, urllib.parse, re, csv, sys
import xml.etree.ElementTree as ET
base="https://zoekservice.overheid.nl/sru/Search"
q=sys.argv[1]
out=sys.argv[2]
rows=[]
start=1
while True:
    params={"x-connection":"cvdr","operation":"searchRetrieve","version":"1.2","query":q,"startRecord":str(start),"maximumRecords":"100"}
    url=base+"?"+urllib.parse.urlencode(params)
    data=urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=60).read()
    root=ET.fromstring(data)
    ns={'s':'http://www.loc.gov/zing/srw/'}
    n=int(root.find('s:numberOfRecords',ns).text)
    recs=root.findall('.//s:record',ns)
    if not recs: break
    for r in recs:
        d={}
        for el in r.iter():
            tag=el.tag.split('}')[1]
            if el.text and el.text.strip():
                d.setdefault(tag,[]).append(el.text.strip())
        rows.append(d)
    start+=len(recs)
    if start>n: break
print(n,len(rows))
keys=["identifier","title","creator","type","modified","issued","available","validFrom","isRatifiedBy","subject","source","publisher","rights","isFormatOf","hasVersion","isReplacedBy"]
allk=sorted({k for d in rows for k in d})
print(allk)
import json
json.dump(rows,open(out,"w"))
