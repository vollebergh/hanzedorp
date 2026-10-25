import urllib.request, urllib.parse, json, sys, time
import xml.etree.ElementTree as ET
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
ns={'sru':'http://docs.oasis-open.org/ns/search-ws/sruResponse','dc':'http://purl.org/dc/terms/','ow':'http://standaarden.overheid.nl/wetgeving/','gzd':'http://standaarden.overheid.nl/sru'}
q=sys.argv[1]; outf=sys.argv[2]
out=[]; start=1; total=None
while True:
    params=urllib.parse.urlencode({'version':'2.0','operation':'searchRetrieve','x-connection':'officielepublicaties','query':q,'maximumRecords':'1000','startRecord':str(start)})
    req=urllib.request.Request('https://repository.overheid.nl/sru?'+params,headers={'User-Agent':UA})
    for attempt in range(4):
        try:
            data=urllib.request.urlopen(req,timeout=120).read(); break
        except Exception as e:
            print('retry',e); time.sleep(3)
    root=ET.fromstring(data)
    if total is None:
        total=int(root.find('.//sru:numberOfRecords',ns).text); print('total',total)
    recs=root.findall('.//sru:record',ns)
    if not recs: break
    for r in recs:
        g=lambda p:(r.find('.//'+p,ns).text if r.find('.//'+p,ns) is not None else '')
        out.append(dict(id=g('dc:identifier'),title=g('dc:title'),type=g('dc:type'),date=g('dc:date'),mod=g('dc:modified'),pub=g('ow:publicatienaam'),subject=g('dc:subject')))
    start+=len(recs)
    if start>total: break
json.dump(out,open(outf,'w'),ensure_ascii=False)
print(len(out))
