import urllib.request, urllib.parse, re, sys, os
out=sys.argv[1]; q=sys.argv[2]
start=1; rows=[]
while True:
    url="https://repository.overheid.nl/sru?"+urllib.parse.urlencode({'operation':'searchRetrieve','version':'2.0','x-connection':'officielepublicaties','maximumRecords':'1000','startRecord':str(start),'query':q})
    d=urllib.request.urlopen(url,timeout=300).read().decode()
    n=int(re.findall(r'numberOfRecords>(\d+)<',d)[0])
    recs=re.findall(r'<sru:record>.*?</sru:record>',d,re.S)
    for r in recs:
        g=lambda t:(re.findall(r'<dcterms:'+t+r'[^>]*>(.*?)</dcterms:'+t+'>',r,re.S) or [''])[0].replace('\t',' ').replace('\n',' ')
        rows.append([g('identifier'),g('date'),g('type'),g('creator'),g('title')])
    start+=len(recs)
    print(start,n,file=sys.stderr)
    if not recs or start>n: break
with open(out,'w') as f:
    for r in rows: f.write('\t'.join(r)+'\n')
print(len(rows))
