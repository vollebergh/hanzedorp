import urllib.request,urllib.parse,sys,re,json
UA="Mozilla/5.0 Chrome/130"
q=sys.argv[1]; out=sys.argv[2]
recs=[];start=1
while True:
    u='https://zoekservice.overheid.nl/sru/Search?'+urllib.parse.urlencode({'x-connection':'cvdr','operation':'searchRetrieve','version':'1.2','query':q,'maximumRecords':100,'startRecord':start})
    t=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60).read().decode()
    n=int(re.search(r'numberOfRecords>(\d+)<',t).group(1))
    for r in re.findall(r'<record>(.*?)</record>',t,re.S):
        g=lambda tag: (re.search(r'<[^>]*'+tag+r'[^>]*>(.*?)</',r,re.S) or [None,''])[1]
        recs.append(dict(id=g('dcterms:identifier'),title=g('dcterms:title'),creator=g('dcterms:creator'),issued=g('dcterms:issued'),modified=g('dcterms:modified'),inwerking=g('inwerkingtredingDatum'),uitwerking=g('uitwerkingtredingDatum')))
    start+=100
    if start>n: break
json.dump(recs,open(out,'w'),ensure_ascii=False)
print(n,len(recs))
