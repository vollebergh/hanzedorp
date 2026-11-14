import sys, urllib.request, urllib.parse, xml.etree.ElementTree as ET, json
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36'
def fetch(q, start, n=100):
    p=urllib.parse.urlencode({'version':'1.2','operation':'searchRetrieve','x-connection':'cvdr','query':q,'maximumRecords':n,'startRecord':start})
    r=urllib.request.Request('https://zoekservice.overheid.nl/sru/Search?'+p,headers={'User-Agent':UA})
    return urllib.request.urlopen(r,timeout=60).read()
ns={'s':'http://www.loc.gov/zing/srw/','d':'http://purl.org/dc/terms/','o':'http://standaarden.overheid.nl/cvdr/terms/','g':'http://standaarden.overheid.nl/sru'}
def run(q):
    out=[];start=1
    while True:
        x=ET.fromstring(fetch(q,start))
        tot=int(x.find('s:numberOfRecords',ns).text)
        recs=x.findall('.//s:record',ns)
        for r in recs:
            def t(path):
                e=r.find(path,ns); return e.text if e is not None else ''
            out.append(dict(id=t('.//d:identifier'),title=t('.//d:title'),type=t('.//d:type'),creator=t('.//d:creator'),
              modified=t('.//d:modified'),issued=t('.//d:issued'),inw=t('.//o:inwerkingtredingDatum'),uitw=t('.//o:uitwerkingtredingDatum'),
              betreft=t('.//o:betreft'),alt=t('.//d:alternative'),kenmerk=t('.//o:kenmerk'),src=t('.//d:isFormatOf'),subj=t('.//d:subject'),
              url=t('.//d:identifier')))
        start+=len(recs)
        if not recs or start>tot: break
    return out
if __name__=='__main__':
    q=sys.argv[1]
    o=run(q)
    json.dump(o,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
    print(len(o))
