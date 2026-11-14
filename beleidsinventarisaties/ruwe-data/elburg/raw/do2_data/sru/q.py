import sys,urllib.request,urllib.parse,re
q=sys.argv[1]; n=sys.argv[2] if len(sys.argv)>2 else '60'
u='https://repository.overheid.nl/sru?'+urllib.parse.urlencode({'version':'2.0','operation':'searchRetrieve','query':q,'maximumRecords':n})
t=urllib.request.urlopen(u,timeout=60).read().decode()
print(re.findall(r'<sru:numberOfRecords>(\d+)',t))
for r in t.split('<sru:record>')[1:]:
    ti=re.findall(r'<dcterms:title>([^<]*)',r); d=re.findall(r'<dcterms:available>([^<]*)|<dcterms:issued>([^<]*)',r); i=re.findall(r'<dcterms:identifier>([^<]*)',r)
    print(i[:1],[x for y in d[:1] for x in y if x],ti[:1])
