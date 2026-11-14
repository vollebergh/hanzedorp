import sys,re,urllib.parse,subprocess
q=sys.argv[1]; n=sys.argv[2] if len(sys.argv)>2 else '30'
url="https://repository.overheid.nl/sru?operation=searchRetrieve&version=2.0&x-connection=officielepublicaties&maximumRecords="+n+"&query="+urllib.parse.quote(q)
t=subprocess.run(['curl','-s','--max-time','90',url],capture_output=True,text=True).stdout
print(re.findall(r'numberOfRecords>(\d+)',t), re.findall(r'<diag:message>(.*?)<',t))
for r in re.findall(r'<sru:recordData>(.*?)</sru:recordData>',t,re.S):
    g=lambda p:re.sub(r'\s+',' ',(re.search(p,r,re.S) or [None,''])[1]).strip()
    print(' ',g(r'<dcterms:identifier>(.*?)<'),'|',g(r'<dcterms:title>(.*?)</dcterms:title>')[:130],'|',g(r'<dcterms:available>(.*?)<'),'|',g(r'<dcterms:creator[^>]*>(.*?)<'))
