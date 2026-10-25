import re,html,subprocess,sys,json,os,time
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
out=sys.argv[1]
base='https://www.hardenberg.nl'
url=base+'/nieuws'
items=[];seen=set();n=0
while url and n<120:
    n+=1
    s=subprocess.run(['curl','-sL','-A',UA,url],capture_output=True,text=True).stdout
    for href,body in re.findall(r'href="(/nieuws/nieuwsbericht/artikel/[^"]+)"[^>]*>(.*?)</a>',s,re.S):
        t=' '.join(html.unescape(re.sub('<[^>]+>',' ',body)).split())
        if href not in seen:
            seen.add(href); items.append({'url':base+href,'text':t})
    m=re.search(r'href="([^"]+)"[^>]*>\s*Volgende',s)
    url=base+html.unescape(m.group(1)) if m else None
    time.sleep(0.3)
json.dump(items,open(out,'w'),ensure_ascii=False,indent=0)
print(n,len(items))
