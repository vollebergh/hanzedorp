import sys,subprocess,re,html,json,os
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
for u in sys.argv[1:]:
    s=subprocess.run(['curl','-sL','-A',UA,u],capture_output=True,text=True).stdout
    date=re.findall(r'"datePublished"\s*:\s*"([^"]+)"',s)
    title=re.search(r'<title>(.*?)</title>',s,re.S)
    # try JSON-LD articleBody
    body=re.findall(r'"articleBody"\s*:\s*"((?:[^"\\]|\\.)*)"',s)
    if body: txt=json.loads('"'+body[0]+'"')
    else:
        b=re.sub(r'<(script|style|nav|footer|header)[^>]*>.*?</\1>','',s,flags=re.S)
        ps=re.findall(r'<p[^>]*>(.*?)</p>',b,re.S)
        txt='\n'.join(' '.join(html.unescape(re.sub('<[^>]+>','',p)).split()) for p in ps)
    fn=re.sub(r'[^a-z0-9]+','_',u.split('/nieuws/')[-1].lower())[:80]+'.txt'
    open(fn,'w').write(u+'\nDATE: '+(date[0] if date else '?')+'\nTITLE: '+(html.unescape(title.group(1)) if title else '?')+'\n'+txt)
    print(fn,date[:1],len(txt))
