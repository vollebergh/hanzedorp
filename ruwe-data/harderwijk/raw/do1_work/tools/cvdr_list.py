import urllib.request,urllib.parse,re,sys,html,os
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA='Mozilla/5.0 (X11; Linux x86_64) Chrome/130.0.0.0 Safari/537.36'
rows=[];start=1
while True:
    q=urllib.parse.quote('dcterms.creator=Harderwijk')
    u=f"https://zoekservice.overheid.nl/sru/Search?x-connection=cvdr&operation=searchRetrieve&version=1.2&query={q}&maximumRecords=100&startRecord={start}"
    x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60).read().decode()
    n=int(re.search(r'numberOfRecords>(\d+)',x).group(1))
    recs=re.findall(r'<overheidrg:meta.*?</overheidrg:meta>',x,re.S)
    for r in recs:
        g=lambda t:(re.search(r'<%s[^>]*>(.*?)</%s>'%(t,t),r,re.S) or [None,''])[1].strip()
        rows.append((g('dcterms:identifier'),g('dcterms:creator'),g('dcterms:issued'),g('overheidrg:inwerkingtredingDatum'),g('overheidrg:uitwerkingtredingDatum'),html.unescape(g('dcterms:title'))[:200],g('dcterms:type'),g('dcterms:modified')))
    if not recs: break
    start+=len(recs)
    if start>n: break
open(W+'/cvdr_harderwijk.tsv','w').write("\n".join("\t".join(r) for r in rows))
print(n,len(rows))
