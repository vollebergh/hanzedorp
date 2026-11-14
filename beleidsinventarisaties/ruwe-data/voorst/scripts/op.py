import sys,urllib.request,urllib.parse,xml.etree.ElementTree as ET,json,re
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36'
ns={'s':'http://docs.oasis-open.org/ns/search-ws/sruResponse','d':'http://purl.org/dc/terms/'}
def run(q,maxn=100,limit=5000,quiet=False):
    out=[];start=1;tot=None
    while True:
        p=urllib.parse.urlencode({'query':'(c.product-area==officielepublicaties) and ('+q+')','maximumRecords':maxn,'startRecord':start})
        r=urllib.request.Request('https://repository.overheid.nl/sru?'+p,headers={'User-Agent':UA})
        raw=urllib.request.urlopen(r,timeout=90).read()
        x=ET.fromstring(raw)
        tot=int(x.find('s:numberOfRecords',ns).text)
        recs=x.findall('.//s:record',ns)
        for rec in recs:
            def t(tag):
                e=rec.find('.//d:'+tag,ns); return e.text if e is not None else ''
            pu=''
            for e in rec.iter():
                if e.tag.endswith('preferredUrl'): pu=e.text
            hv=''
            e=rec.find('.//d:hasVersion',ns)
            if e is not None: hv=e.get('resourceIdentifier') or ''
            out.append(dict(id=t('identifier'),title=t('title'),type=t('type'),creator=t('creator'),date=t('available') or t('modified'),url=pu or hv,subject=t('subject')))
        start+=len(recs)
        if not recs or start>tot or start>limit: break
    if not quiet: print('total',tot,'got',len(out))
    return out
if __name__=='__main__':
    for q in sys.argv[1:]:
        print('##',q)
        for x in sorted(run(q),key=lambda x:x['date']): print(' ',x['id'],x['date'],'|',x['title'][:170])
