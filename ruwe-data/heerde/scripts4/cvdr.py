import sys, re, json, urllib.request, urllib.parse, xml.etree.ElementTree as ET
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
out=sys.argv[1]
ns={'d':'http://purl.org/dc/terms/','o':'http://standaarden.overheid.nl/owms/terms/','r':'http://standaarden.overheid.nl/cvdr/terms/','z':'http://www.loc.gov/zing/srw/','g':'http://standaarden.overheid.nl/sru'}
recs=[];start=1
while True:
    q=urllib.parse.urlencode({'x-connection':'cvdr','operation':'searchRetrieve','version':'1.2','query':'dcterms.creator=Heerde','maximumRecords':'100','startRecord':str(start)})
    req=urllib.request.Request('https://zoekservice.overheid.nl/sru/Search?'+q,headers={'User-Agent':UA})
    x=urllib.request.urlopen(req,timeout=60).read()
    root=ET.fromstring(x)
    n=int(root.find('z:numberOfRecords',ns).text)
    rs=root.findall('.//z:record',ns)
    if not rs: break
    for r in rs:
        def t(p):
            e=r.find(p,ns); return e.text if e is not None else None
        d={'id':t('.//d:identifier'),'title':t('.//d:title'),'type':t('.//d:type'),'modified':t('.//d:modified'),
           'issued':t('.//d:issued'),'inwerking':t('.//r:inwerkingtredingDatum'),'uitwerking':t('.//r:uitwerkingtredingDatum'),
           'betreft':t('.//r:betreft'),'subject':t('.//d:subject'),'isFormatOf':t('.//d:isFormatOf'),'ratified':t('.//o:isRatifiedBy'),
           'creator':t('.//d:creator'),'alt':t('.//d:alternative'),'kenmerk':t('.//r:kenmerk')}
        # url
        u=r.find('.//g:preferredUrl',ns); d['url']=u.text if u is not None else None
        recs.append(d)
    start+=len(rs)
    if start>n: break
json.dump(recs,open(out,'w'),ensure_ascii=False,indent=1)
print(len(recs))
