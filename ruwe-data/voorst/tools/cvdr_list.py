import subprocess,re,json,html
UA=open('ua.txt').read().strip()
out={}
start=1
while True:
    url=f"https://zoekservice.overheid.nl/sru/Search?version=1.2&operation=searchRetrieve&x-connection=cvdr&startRecord={start}&maximumRecords=100&query=dcterms.creator%3DVoorst"
    r=subprocess.run(['curl','-sL','-A',UA,'--max-time','60',url],capture_output=True).stdout.decode('utf8','replace')
    recs=r.split('<record>')[1:]
    if not recs: 
        print('stop at',start, r[:200]); break
    for rec in recs:
        ident=re.search(r'<dcterms:identifier>([^<]*)<',rec)
        title=re.search(r'<dcterms:title>([^<]*)<',rec)
        creator=re.findall(r'<dcterms:creator[^>]*>([^<]*)<',rec)
        mod=re.search(r'<dcterms:modified>([^<]*)<',rec)
        issued=re.search(r'<dcterms:issued>([^<]*)<',rec)
        eind=re.search(r'<overheidrg:uitwerkingtredingDatum>([^<]*)<',rec)
        begin=re.search(r'<overheidrg:inwerkingtredingDatum>([^<]*)<',rec)
        out[ident.group(1) if ident else str(len(out))]={'title':html.unescape(title.group(1)) if title else None,'creator':creator,'issued':issued.group(1) if issued else None,'modified':mod.group(1) if mod else None,'begin':begin.group(1) if begin else None,'eind':eind.group(1) if eind else None}
    n=re.search(r'numberOfRecords>(\d+)<',r)
    total=int(n.group(1)) if n else 0
    print(start,len(recs),total)
    start+=100
    if start>total: break
json.dump(out,open('d1/cvdr/voorst_list.json','w'))
print(len(out))
