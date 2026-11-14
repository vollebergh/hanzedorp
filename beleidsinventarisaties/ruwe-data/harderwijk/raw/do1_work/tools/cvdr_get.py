import sys,re,html,os,urllib.request
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA='Mozilla/5.0 (X11; Linux x86_64) Chrome/130.0.0.0 Safari/537.36'
for arg in sys.argv[1:]:
    m=re.match(r'CVDR(\d+)_(\d+)',arg); n,v=m.group(1),m.group(2)
    u=f"https://repository.officiele-overheidspublicaties.nl/cvdr/CVDR{n}/{v}/xml/CVDR{n}_{v}.xml"
    x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60).read().decode('utf8','ignore')
    t=re.sub(r'</(p|li|al|nadruk|titel|kop|tr|row|lid|artikel)>','\n',x); t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t)
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(f"{W}/cvdr/CVDR{n}_{v}.txt","w").write(t); print(arg,len(t))
