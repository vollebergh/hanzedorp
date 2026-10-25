import urllib.request,urllib.parse,sys
import xml.etree.ElementTree as ET
UA=open('ua.txt').read().strip()
def q(query,maxr=100):
    out=[];start=1
    while True:
        p=urllib.parse.urlencode({'x-connection':'officielepublicaties','operation':'searchRetrieve','version':'2.0','query':query,'maximumRecords':str(maxr),'startRecord':str(start)})
        x=urllib.request.urlopen(urllib.request.Request('https://repository.overheid.nl/sru?'+p,headers={'User-Agent':UA}),timeout=90).read()
        root=ET.fromstring(x)
        recs=[e for e in root.iter() if e.tag.endswith('}record')]
        tot=[e.text for e in root.iter() if e.tag.endswith('numberOfRecords')]
        if not recs: break
        for r in recs:
            d={}
            for e in r.iter():
                t=e.tag.split('}')[1]
                if e.text and e.text.strip() and t in('identifier','title','type','publicationName','date','modified','available','creator','authority','subject','alternative','issued','preferredUrl'):
                    d.setdefault(t,[]).append(e.text.strip())
            out.append(d)
        start+=len(recs)
        if len(recs)<maxr or start>600: break
    return tot,out
if __name__=='__main__':
    tot,o=q(sys.argv[1], 50)
    print(tot,len(o))
    for d in o: print(d.get('date',d.get('available',['']))[0] if d.get('date') or d.get('available') else '', d.get('identifier',[''])[0], '|', d.get('title',[''])[0][:160], '|', d.get('type',[''])[0])
