import sys, json, urllib.request, urllib.parse, xml.etree.ElementTree as ET
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
query=sys.argv[1]; out=sys.argv[2]
ns={'d':'http://purl.org/dc/terms/','w':'http://standaarden.overheid.nl/wetgeving/','s':'http://docs.oasis-open.org/ns/search-ws/sruResponse','g':'http://standaarden.overheid.nl/sru'}
recs=[];start=1
while True:
    q=urllib.parse.urlencode({'version':'2.0','x-connection':'officielepublicaties','operation':'searchRetrieve','query':query,'maximumRecords':'1000','startRecord':str(start)})
    x=urllib.request.urlopen(urllib.request.Request('https://repository.overheid.nl/sru?'+q,headers={'User-Agent':UA}),timeout=180).read()
    root=ET.fromstring(x)
    n=int(root.find('s:numberOfRecords',ns).text)
    rs=root.findall('.//s:record',ns)
    if not rs: break
    for r in rs:
        def t(p):
            e=r.find(p,ns); return e.text if e is not None else None
        recs.append({'id':t('.//d:identifier'),'title':t('.//d:title'),'rubriek':t('.//d:type'),'date':t('.//d:date'),'abstract':t('.//d:abstract'),
           'blad':t('.//w:publicatienaam'),'url':t('.//g:preferredUrl'),'subject':t('.//d:subject')})
    start+=len(rs)
    print(start,n,file=sys.stderr)
    if start>n: break
json.dump(recs,open(out,'w'),ensure_ascii=False,indent=0)
print(len(recs))
