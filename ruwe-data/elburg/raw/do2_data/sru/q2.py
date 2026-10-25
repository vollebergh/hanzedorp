import urllib.request,urllib.parse,re,json
q='dt.creator="Gelderland" AND cql.textAndIndexes="Elburg"'
out=[]
for s in range(1,400,100):
    u='https://repository.overheid.nl/sru?'+urllib.parse.urlencode({'version':'2.0','operation':'searchRetrieve','query':q,'maximumRecords':100,'startRecord':s})
    t=urllib.request.urlopen(u,timeout=90).read().decode()
    for r in t.split('<sru:record>')[1:]:
        ti=re.findall(r'<dcterms:title>([^<]*)',r); d=re.findall(r'<dcterms:available>([^<]*)',r) or re.findall(r'<dcterms:issued>([^<]*)',r); i=re.findall(r'<dcterms:identifier>([^<]*)',r)
        out.append((d[0] if d else '',i[0] if i else '',ti[0] if ti else ''))
json.dump(out,open('prb_elburg_all.json','w'),ensure_ascii=False,indent=0)
print(len(out))
kw=re.compile(r'zienswijze|ontheffing|afwijk|instemming|BOPA|buitenplans|omgevingsverordening|woningen|woonafspraken|wonen|Natura 2000|N2000|Flora',re.I)
for d,i,t in sorted(out,reverse=True):
    if d>='2022' and kw.search(t): print(d,i,t[:170])
