import sys,urllib.request,urllib.parse,re,html
import xml.etree.ElementTree as ET
term=sys.argv[1]; extra=sys.argv[2] if len(sys.argv)>2 else ''
q=f'dt.creator=Harderwijk AND cql.textAndIndexes="{term}"'+extra
start=1;tot=None;n=0
while True:
    p={"x-connection":"officielepublicaties","operation":"searchRetrieve","version":"2.0","query":q,"startRecord":str(start),"maximumRecords":"50"}
    url="https://repository.overheid.nl/sru?"+urllib.parse.urlencode(p)
    try: d=urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=60).read()
    except Exception as e: print('ERR',e); break
    root=ET.fromstring(d)
    ns={'s':'http://docs.oasis-open.org/ns/search-ws/sruResponse'}
    tn=root.find('s:numberOfRecords',ns)
    tot=int(tn.text) if tn is not None else 0
    recs=root.findall('.//s:record',ns)
    if not recs: break
    for r in recs:
        txt={}
        for el in r.iter():
            t=el.tag.split('}')[1]
            if el.text and el.text.strip(): txt.setdefault(t,[]).append(el.text.strip())
        print(' | '.join([ (txt.get('identifier') or ['?'])[0], (txt.get('date') or txt.get('available') or ['?'])[0], (txt.get('title') or ['?'])[0][:130], (txt.get('type') or [''])[0]]))
        n+=1
    start+=len(recs)
    if start>tot or n>=int(sys.argv[3]) if len(sys.argv)>3 else n>=100: break
print('totaal',tot)
