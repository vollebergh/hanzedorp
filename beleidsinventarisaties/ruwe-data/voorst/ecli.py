import sys,json,re,html,urllib.request
e=sys.argv[1]
req=urllib.request.Request('https://uitspraken.rechtspraak.nl/api/document/?id='+e,headers={'User-Agent':'Mozilla/5.0'})
d=json.load(urllib.request.urlopen(req))
c=lambda s: re.sub(r'\n\s*\n+','\n',html.unescape(re.sub(r'<[^>]+>','\n',s or '')))
print(d['CitaatText'], d['DatumUitspraak'], d['Zaaknummer'])
print(c(d['InhoudsindicatieTekst']))
open(sys.argv[2],'w').write(c(d['UitspraakTekst']))
