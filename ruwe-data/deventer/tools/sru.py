import sys,requests,re,html
q=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 100
start=1; tot=None; out=[]
while True:
    r=requests.get('https://repository.overheid.nl/sru',params={'operation':'searchRetrieve','version':'2.0','x-connection':'officielepublicaties','query':q,'maximumRecords':min(n,100),'startRecord':start},headers={'User-Agent':'Mozilla/5.0'},timeout=120)
    t=r.text
    if tot is None:
        m=re.search(r'numberOfRecords>(\d+)<',t); tot=int(m.group(1)) if m else 0; print('total',tot)
    recs=re.findall(r'<sru:record>(.*?)</sru:record>',t,re.S)
    for rec in recs:
        def g(tag):
            m=re.search(r'<'+tag+r'[^>]*>(.*?)</'+tag+'>',rec,re.S); return html.unescape(m.group(1)).strip() if m else ''
        out.append((g('dcterms:available') or g('dcterms:issued'), g('dcterms:identifier'), g('dcterms:creator'), g('dcterms:title')[:200]))
    start+=len(recs)
    if not recs or start>tot or start>n: break
for o in sorted(out): print(' | '.join(o))
