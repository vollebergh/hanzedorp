import sys,re,urllib.parse,subprocess
q=sys.argv[1]; conn=sys.argv[2] if len(sys.argv)>2 else 'officielepublicaties'
url=f"https://zoekservice.overheid.nl/sru/Search?x-connection={conn}&operation=searchRetrieve&version=1.2&maximumRecords=40&query="+urllib.parse.quote(q)
t=subprocess.run(['curl','-s','--max-time','60',url],capture_output=True,text=True).stdout
print(re.findall(r'<numberOfRecords>(\d+)',t), re.findall(r'<message>(.*?)</message>',t))
for r in re.findall(r'<recordData>(.*?)</recordData>',t,re.S):
    g=lambda p:re.sub(r'\s+',' ',(re.search(p,r,re.S) or [None,''])[1]).strip()
    print(' ',g(r'<dcterms:identifier>(.*?)<'),'|',g(r'<dcterms:title>(.*?)</dcterms:title>')[:120],'|',g(r'<dcterms:available>(.*?)<') or g(r'<dcterms:date>(.*?)<'),'|',g(r'<dcterms:creator[^>]*>(.*?)<'))
