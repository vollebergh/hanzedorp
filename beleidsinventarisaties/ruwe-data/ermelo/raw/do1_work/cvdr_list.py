#!/usr/bin/env python3
import urllib.request, urllib.parse, re, sys, html
UA='Mozilla/5.0 (X11; Linux x86_64) Chrome/124.0.0.0'
out=[]; start=1
while True:
    q={'version':'1.2','operation':'searchRetrieve','x-connection':'cvdr','query':'dcterms.creator=Ermelo','maximumRecords':'100','startRecord':str(start)}
    u='https://zoekservice.overheid.nl/sru/Search?'+urllib.parse.urlencode(q)
    x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60).read().decode()
    recs=re.findall(r'<record>(.*?)</record>',x,re.S)
    if not recs: break
    for r in recs:
        g=lambda tag: (re.search(r'<%s[^>]*>(.*?)</%s>'%(tag,tag),r,re.S) or [None,''])[1]
        ident=g('dcterms:identifier'); title=html.unescape(g('dcterms:title')); mod=g('dcterms:modified')
        alt=html.unescape(g('dcterms:alternative'))
        ist=g('overheidrg:inwerkingtreding') or g('dcterms:valid')
        beg=re.search(r'<overheidrg:inwerkingtredingDatum>(.*?)<',r) 
        uit=re.search(r'<overheidrg:uitwerkingtredingDatum>(.*?)<',r)
        out.append((ident,mod,beg.group(1) if beg else '',uit.group(1) if uit else '',title,alt))
    start+=100
    if start>3000: break
with open(sys.argv[1],'w') as f:
    for o in out: f.write('\t'.join(o)+'\n')
print(len(out))
