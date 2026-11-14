import sys,urllib.request,urllib.parse
import xml.etree.ElementTree as ET
q=sys.argv[1]
start=1;n=0
while True:
    p={"x-connection":"officielepublicaties","operation":"searchRetrieve","version":"2.0","query":q,"startRecord":str(start),"maximumRecords":"50"}
    d=urllib.request.urlopen(urllib.request.Request("https://repository.overheid.nl/sru?"+urllib.parse.urlencode(p),headers={"User-Agent":"Mozilla/5.0"}),timeout=60).read()
    root=ET.fromstring(d); ns={'s':'http://docs.oasis-open.org/ns/search-ws/sruResponse'}
    tot=int(root.find('s:numberOfRecords',ns).text); recs=root.findall('.//s:record',ns)
    if not recs: break
    for r in recs:
        txt={}
        for el in r.iter():
            t=el.tag.split('}')[1]
            if el.text and el.text.strip(): txt.setdefault(t,[]).append(el.text.strip())
        print(' | '.join([(txt.get('identifier') or ['?'])[0],(txt.get('date') or txt.get('available') or ['?'])[0],(txt.get('title') or ['?'])[0][:150]]))
        n+=1
    start+=len(recs)
    if start>tot: break
print('totaal',tot)
