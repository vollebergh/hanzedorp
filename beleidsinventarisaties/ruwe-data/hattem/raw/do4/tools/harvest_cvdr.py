import sys, urllib.request, urllib.parse, re, json, time
import xml.etree.ElementTree as ET
out=sys.argv[1]; q=sys.argv[2]; conn=sys.argv[3] if len(sys.argv)>3 else 'cvdr'
base={'cvdr':'https://zoekservice.overheid.nl/sru/Search','officielepublicaties':'https://repository.overheid.nl/sru'}[conn]
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
recs=[]; start=1; n=None
while True:
    params={'x-connection':conn,'operation':'searchRetrieve','version':'1.2','query':q,'startRecord':start,'maximumRecords':100}
    url=base+'?'+urllib.parse.urlencode(params)
    data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=120).read()
    root=ET.fromstring(data)
    if n is None:
        n=int(root.find('{http://www.loc.gov/zing/srw/}numberOfRecords').text); print('total',n,file=sys.stderr)
    rs=root.findall('.//{http://www.loc.gov/zing/srw/}record')
    if not rs: break
    for r in rs:
        d={}
        for el in r.iter():
            tag=el.tag.split('}')[-1]
            t=(el.text or '').strip()
            if t and tag not in d: d[tag]=t
            elif t and tag in d and tag in ('subject','url','itemUrl'): d[tag]+=' | '+t
        # keep itemUrl list
        d['_urls']=[ (el.attrib.get('manifestation'), (el.text or '').strip()) for el in r.iter() if el.tag.endswith('itemUrl')]
        recs.append(d)
    start+=len(rs)
    if start>n: break
    time.sleep(0.3)
json.dump(recs,open(out,'w'),ensure_ascii=False,indent=0)
print(len(recs),file=sys.stderr)
