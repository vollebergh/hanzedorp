"""SRU officielepublicaties. Usage: python3 -I sru.py '<cql>' outfile"""
import urllib.request,urllib.parse,re,sys
qry,out=sys.argv[1],sys.argv[2]
rows=[];start=1
while True:
    u="https://repository.overheid.nl/sru?"+urllib.parse.urlencode({"query":qry,"maximumRecords":1000,"startRecord":start,"x-connection":"officielepublicaties"})
    x=urllib.request.urlopen(u,timeout=180).read().decode()
    tot=int(re.search(r"numberOfRecords>(\d+)",x).group(1))
    for rec in x.split("<sru:record>")[1:]:
        g=lambda p:(re.search(p,rec,re.S) or [None,""])[1]
        rows.append((g(r"<dcterms:date>([^<]*)"),g(r"<dcterms:identifier>([^<]+)"),g(r"<dcterms:type[^>]*>([^<]*)"),g(r"<dcterms:title>([^<]+)").replace("\n"," ")))
    start+=1000
    if start>tot: break
rows.sort(reverse=True)
open(out,"w").write("\n".join("\t".join(r) for r in rows))
print(tot,len(rows))
