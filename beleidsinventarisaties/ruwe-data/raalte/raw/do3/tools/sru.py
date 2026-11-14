import sys,urllib.request,urllib.parse,re,html,os
q=sys.argv[1]; fetch=len(sys.argv)>2; out=[]; start=1
while True:
    url='https://repository.overheid.nl/sru?'+urllib.parse.urlencode({'query':q,'maximumRecords':'100','startRecord':str(start)})
    t=urllib.request.urlopen(url,timeout=60).read().decode('utf-8','ignore')
    for r in re.findall(r'<sru:record>(.*?)</sru:record>',t,re.S):
        g=lambda p: (re.search(p,r,re.S).group(1) if re.search(p,r,re.S) else '')
        out.append((g(r'<dcterms:identifier>(.*?)</dcterms:identifier>'),g(r'<dcterms:date>(.*?)</dcterms:date>'),html.unescape(g(r'<dcterms:title>(.*?)</dcterms:title>')),g(r'<gzd:url>(.*?)</gzd:url>')))
    n=int(re.search(r'<sru:numberOfRecords>(\d+)',t).group(1)); start+=100
    if start>n or start>2000: break
print(n,file=sys.stderr)
for o in sorted(set(out),key=lambda x:x[1]):
    print('\t'.join(o[:3]))
    if fetch:
        fn='gmb/'+o[0]+'.txt'
        if not os.path.exists(fn):
            x=urllib.request.urlopen(o[3],timeout=60).read().decode('utf-8','ignore')
            x=re.sub(r'<[^>]+>',' ',x); x=html.unescape(re.sub(r'\s+',' ',x))
            open(fn,'w').write(x)
