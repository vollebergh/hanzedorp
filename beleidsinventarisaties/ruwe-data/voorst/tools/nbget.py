import json,sys,subprocess,os,re
m=json.load(open('d1/notubiz/modules.json'))
D='d1/nbdocs'; os.makedirs(D,exist_ok=True)
UA=open('ua.txt').read().strip()
byid={}
for mod,its in m.items():
    for it in its: byid[(mod,str(it['id']))]=it
for arg in sys.argv[1:]:
    mod,iid=arg.split(':')
    it=byid.get((mod,iid))
    if not it: print('missing',arg); continue
    t=(it.get('titel') or it.get('Onderwerp') or it.get('Titel') or '')
    print('###',arg,t.replace('\n',' ')[:100])
    for i,d in enumerate(it['docs']):
        did=re.search(r'document/(\d+)/(\d+)',d['url'])
        name=f"{mod}_{iid}_{i}"
        path=f"{D}/{name}.bin"
        r=subprocess.run(['curl','-sL','-A',UA,'--max-time','120','-o',path,'-w','%{http_code} %{content_type}',d['url']],capture_output=True)
        typ=subprocess.run(['file','-b',path],capture_output=True).stdout.decode()[:40]
        txt=''
        if 'PDF' in typ:
            subprocess.run(['python3','-I','tools/pdf2txt.py',path,f"{D}/{name}.txt"])
            txt=f"{D}/{name}.txt"; wc=len(open(txt).read().split())
        else: wc=-1
        print('   ',name,d.get('title','')[:80],'|',typ,'|',wc)
