import sys,re,urllib.parse,subprocess
q=sys.argv[1]
url="https://zoekservice.overheid.nl/sru/Search?x-connection=cvdr&operation=searchRetrieve&version=1.2&maximumRecords=50&query="+urllib.parse.quote(q)
t=subprocess.run(['curl','-s','--max-time','60',url],capture_output=True,text=True).stdout
if '<diagnostic' in t: print(re.findall(r'<message>(.*?)</message>',t)); 
for r in re.findall(r'<sru:recordData>(.*?)</sru:recordData>',t,re.S):
    g=lambda p: (re.search(p,r,re.S) or [None,''])[1]
    print(' ',g(r'<dcterms:identifier>(.*?)</dcterms:identifier>'),'|',g(r'<dcterms:title>(.*?)</dcterms:title>')[:100],'|',g(r'<dcterms:creator[^>]*>(.*?)</dcterms:creator>'),'| in:',g(r'inwerkingtredingDatum[^>]*>(.*?)<'),'uit:',g(r'uitwerkingtredingDatum[^>]*>(.*?)<'))
