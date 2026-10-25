import re,sys,html,subprocess,urllib.parse
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
def get(u):
    return subprocess.run(['curl','-s','-L','--max-time','40','-A',UA,u],capture_output=True).stdout.decode('utf8','ignore')
site=sys.argv[1]; q=sys.argv[2]; pages=int(sys.argv[3]) if len(sys.argv)>3 else 1
seen=set()
for p in range(1,pages+1):
    t=get(f'https://{site}/zoek?q='+urllib.parse.quote(q)+f'&page={p}')
    found=0
    for m in re.finditer(r'<a[^>]+href="((?:https://[^"]*)?/nieuws/[^"]+)"[^>]*>(.*?)</a>',t,flags=re.S):
        u=m.group(1); txt=html.unescape(re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',m.group(2)))).strip()
        if u in seen or not txt: continue
        seen.add(u); found+=1; print(txt[:140],'|',u)
    if not found: break
