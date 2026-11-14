import json,urllib.request,sys,os,re,subprocess
UA="Mozilla/5.0 Chrome/130"
D=sys.argv[1]; ids=sys.argv[2:]
os.makedirs(f'{D}/rv',exist_ok=True)
def get(url): return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=120).read()
for iid in ids:
    d=json.loads(get(f'https://api.notubiz.nl/modules/0/items/{iid}?format=json&version=1.10.8'))
    s=json.dumps(d,ensure_ascii=False)
    docs=re.findall(r'"title": "([^"]+)", "filetype": "(\w+)", "url": "([^"]+)"',s)
    docs+= [(t,ft,u) for (ft,t,u) in re.findall(r'"filetype": "(\w+)", "title": "([^"]+)", "url": "([^"]+)"',s)]
    for t,ft,u in docs:
        did=u.split('/')[-2]
        fn=f'{D}/rv/{iid}_{did}.{ft}'
        if not os.path.exists(fn):
            open(fn,'wb').write(get(u))
        txt=fn+'.txt'
        if not os.path.exists(txt):
            subprocess.run(['python3','-I',os.path.join(os.path.dirname(__file__),'totext.py'),fn,txt],capture_output=True)
        n=len(open(txt).read()) if os.path.exists(txt) else -1
        print(iid,did,ft,n,t,sep='\t')
