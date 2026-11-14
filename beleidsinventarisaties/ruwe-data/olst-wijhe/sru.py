import sys,urllib.request,urllib.parse,re
q=sys.argv[1]; n=sys.argv[2] if len(sys.argv)>2 else '50'
u='https://repository.overheid.nl/sru?'+urllib.parse.urlencode({'query':q,'maximumRecords':n,'httpAccept':'application/xml'})
x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode()
print('total', re.search(r'numberOfRecords>(\d+)<',x).group(1) if re.search(r'numberOfRecords>(\d+)<',x) else '?')
for rec in re.findall(r'<sru:record>(.*?)</sru:record>',x,re.S):
    t=re.search(r'<dcterms:title>(.*?)</dcterms:title>',rec,re.S); i=re.search(r'<dcterms:identifier>(.*?)</dcterms:identifier>',rec); d=re.search(r'<dcterms:available>(.*?)</dcterms:available>',rec)
    c=re.search(r'<dcterms:creator[^>]*>(.*?)</dcterms:creator>',rec)
    print(i.group(1) if i else '', d.group(1) if d else '', c.group(1) if c else '', '|', (t.group(1)[:200] if t else '').replace('\n',' '))
