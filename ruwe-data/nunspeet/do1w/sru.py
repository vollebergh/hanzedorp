import sys,urllib.request,urllib.parse,re,html
q=sys.argv[1];start=sys.argv[2] if len(sys.argv)>2 else '1'
url="https://zoekservice.overheid.nl/sru/Search?x-connection=cvdr&operation=searchRetrieve&version=1.2&maximumRecords=100&startRecord=%s&query=%s"%(start,urllib.parse.quote(q))
d=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})).read().decode()
m=re.search(r'numberOfRecords>(\d+)',d);print('n=',m.group(1) if m else '?')
for r in re.findall(r'<record>.*?</record>',d,flags=re.S):
    g=lambda t:(re.search(r'<dcterms:%s[^>]*>([^<]*)<'%t,r) or [0,''])[1]
    ident=re.search(r'<dcterms:identifier>([^<]*)<',r)
    print(ident.group(1) if ident else '',g('title'),'|',g('creator'),'|',g('modified'), '|', (re.search(r'<overheidrg:uitgever[^>]*>([^<]*)<',r) or [0,''])[1])
