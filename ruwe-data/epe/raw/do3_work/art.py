import sys,re
sys.path.insert(0,'.')
from fetch import fetch, html2text
url=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 3000
d,_=fetch(url); t=d.decode('utf-8','replace')
body=html2text(t)
i=body.find('door Redactie')
j=body.find('Laatste nieuws',i)
print('URL:',url)
print(body[max(0,i-150):(j if j>0 else i+n)][:n])
