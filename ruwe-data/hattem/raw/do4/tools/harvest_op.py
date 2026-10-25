import sys, urllib.request, urllib.parse, json, time
import xml.etree.ElementTree as ET
out=sys.argv[1]; q=sys.argv[2]
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
NS='{http://docs.oasis-open.org/ns/search-ws/sruResponse}'
recs=[]; start=1; n=None
while True:
    params={'operation':'searchRetrieve','version':'2.0','x-connection':'officielepublicaties','query':q,'startRecord':start,'maximumRecords':100}
    url='https://repository.overheid.nl/sru?'+urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=120).read(); break
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(3)
    root=ET.fromstring(data)
    if n is None:
        n=int(root.find(NS+'numberOfRecords').text); print('total',n,file=sys.stderr)
    rs=root.findall('.//'+NS+'record')
    if not rs: break
    for r in rs:
        d={}
        for el in r.iter():
            tag=el.tag.split('}')[-1]; t=(el.text or '').strip()
            if not t: continue
            if tag in d:
                if tag in ('subject','itemUrl','title','type'): d[tag]+=' | '+t
            else: d[tag]=t
        recs.append(d)
    start+=len(rs)
    if start>n: break
    time.sleep(0.2)
json.dump(recs,open(out,'w'),ensure_ascii=False)
print(len(recs),file=sys.stderr)
