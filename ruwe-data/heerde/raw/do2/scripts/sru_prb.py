import urllib.request, urllib.parse, re, json, sys
import xml.etree.ElementTree as ET
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
def sru(q, maxrec=200):
    out=[]; start=1
    while True:
        p={'version':'2.0','operation':'searchRetrieve','x-connection':'officielepublicaties','query':q,'maximumRecords':str(min(maxrec,100)),'startRecord':str(start)}
        u='https://repository.overheid.nl/sru?'+urllib.parse.urlencode(p)
        x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=120).read().decode()
        n=int(re.search(r'<sru:numberOfRecords>(\d+)',x).group(1))
        recs=re.findall(r'<dcterms:identifier>([^<]+)</dcterms:identifier><dcterms:title>([^<]*)</dcterms:title>.*?<dcterms:type[^>]*>([^<]*)</dcterms:type><dcterms:creator[^>]*>([^<]*)</dcterms:creator><dcterms:modified>([^<]*)</dcterms:modified>',x,re.S)
        out+=recs
        start+=100
        if start>n or not recs: break
    return n,out
if __name__=='__main__':
    q=sys.argv[1]
    n,out=sru(q)
    print(n)
    for r in out: print(r[0],'|',r[4],'|',r[2],'|',r[1][:200])
