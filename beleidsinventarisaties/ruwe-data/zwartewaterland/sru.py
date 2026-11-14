import requests, json, sys
from lxml import etree
UA={'User-Agent':'Mozilla/5.0 Chrome/124'}
def sru(q,maxrec=100,limit=3000):
    out=[];start=1
    while True:
        r=requests.get('https://repository.overheid.nl/sru',params={'x-connection':'officielepublicaties','operation':'searchRetrieve','version':'2.0','query':q,'startRecord':start,'maximumRecords':maxrec},headers=UA,timeout=180)
        root=etree.fromstring(r.content)
        ns={'s':'http://docs.oasis-open.org/ns/search-ws/sruResponse'}
        tot=root.find('.//s:numberOfRecords',ns)
        total=int(tot.text) if tot is not None else 0
        recs=root.findall('.//s:record',ns)
        for rec in recs:
            d={}
            for el in rec.iter():
                tag=etree.QName(el).localname
                if el.text and el.text.strip() and tag in('identifier','title','creator','date','type','subject','publicatienaam','organisatietype','url','preferredUrl'):
                    d.setdefault(tag,[]).append(el.text.strip())
            out.append(d)
        start+=maxrec
        if start>total or not recs or start>limit: break
    return total,out
if __name__=='__main__':
    tot,out=sru(sys.argv[1])
    json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False)
    print(tot,len(out))
