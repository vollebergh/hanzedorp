import urllib.request, urllib.parse, re, json, sys
import xml.etree.ElementTree as ET
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
base='https://zoekservice.overheid.nl/sru/Search?x-connection=cvdr&operation=searchRetrieve&version=1.2&query='
q=urllib.parse.quote('dcterms.creator=Oldebroek')
out=[]
start=1
while True:
    url=f'{base}{q}&maximumRecords=100&startRecord={start}'
    req=urllib.request.Request(url,headers={'User-Agent':UA})
    data=urllib.request.urlopen(req,timeout=60).read().decode()
    root=ET.fromstring(data)
    ns={'s':'http://www.loc.gov/zing/srw/','d':'http://purl.org/dc/terms/','o':'http://standaarden.overheid.nl/cvdr/terms/'}
    recs=root.findall('.//s:record',ns)
    if not recs: break
    for r in recs:
        g=lambda p:(r.find('.//'+p,ns).text if r.find('.//'+p,ns) is not None else '')
        out.append(dict(id=g('d:identifier'),title=g('d:title'),creator=g('d:creator'),mod=g('d:modified'),inw=g('o:inwerkingtredingDatum'),uit=g('o:uitwerkingtredingDatum'),type=g('d:type'),subject=g('d:subject'),issued=g('d:issued')))
    start+=100
    if start>1100: break
json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False,indent=0)
print(len(out))
