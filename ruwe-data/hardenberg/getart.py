import json,re,html,subprocess,sys,os
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
d=json.load(open(sys.argv[1])); outdir=sys.argv[2]
for i in map(int,sys.argv[3].split(',')):
    u=d[i]['url']; fn=os.path.join(outdir,'%03d_%s.txt'%(i,u.rstrip('/').split('/')[-1][:60]))
    if os.path.exists(fn): continue
    s=subprocess.run(['curl','-sL','-A',UA,u],capture_output=True,text=True).stdout
    m=re.search(r'<main.*?</main>',s,re.S) or re.search(r'<body.*</body>',s,re.S)
    b=m.group(0) if m else s
    b=re.sub(r'<(script|style|nav|footer)[^>]*>.*?</\1>','',b,flags=re.S)
    b=re.sub(r'</(p|h\d|li|div|tr)>','\n',b)
    t=html.unescape(re.sub(r'<[^>]+>',' ',b))
    t='\n'.join(' '.join(l.split()) for l in t.split('\n') if l.strip())
    open(fn,'w').write(u+'\n'+t)
    print(fn,len(t))
