import urllib.request,urllib.parse,re,sys
def sru(q,n=60):
    url="https://repository.overheid.nl/sru?version=2.0&operation=searchRetrieve&x-connection=officielepublicaties&maximumRecords=%d&query=%s"%(n,urllib.parse.quote(q))
    d=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode()
    m=re.search(r'numberOfRecords>(\d+)',d);print('n=',m.group(1) if m else d[:200])
    out=[]
    for r in re.findall(r'<(?:sru:)?record>.*?</(?:sru:)?record>',d,flags=re.S):
        ti=re.search(r'<dcterms:title>([^<]*)<',r); ide=re.search(r'<dcterms:identifier>([^<]*)<',r); dt=re.search(r'<dcterms:available>([^<]*)<',r) or re.search(r'<dcterms:issued>([^<]*)<',r)
        out.append((dt.group(1) if dt else '', ide.group(1) if ide else '', ti.group(1) if ti else ''))
    for o in sorted(out,reverse=True): print(' | '.join(o))
sru(sys.argv[1], int(sys.argv[2]) if len(sys.argv)>2 else 60)
