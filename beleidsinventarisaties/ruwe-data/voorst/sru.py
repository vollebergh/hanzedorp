import urllib.request,urllib.parse,re,sys,html
def sru(q,n=50):
    u='https://repository.overheid.nl/sru?'+urllib.parse.urlencode({'operation':'searchRetrieve','version':'2.0','query':q,'maximumRecords':str(n)})
    return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode()
term=sys.argv[1]; extra=sys.argv[2] if len(sys.argv)>2 else ''
r=sru(f'dt.creator=="Voorst" AND cql.textAndIndexes="{term}" {extra}')
print('hits',re.search(r'numberOfRecords>(\d+)',r).group(1))
for rec in re.findall(r'<sru:record>(.*?)</sru:record>',r,re.S):
    i=re.search(r'<dcterms:identifier>(.*?)<',rec).group(1)
    t=html.unescape(re.search(r'<dcterms:title>(.*?)<',rec).group(1))
    d=re.search(r'<dcterms:date>(.*?)<',rec)
    print(d.group(1) if d else '?',i,t[:150])
