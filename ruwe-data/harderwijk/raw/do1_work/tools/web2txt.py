import sys,re,os,urllib.request,hashlib
from bs4 import BeautifulSoup
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
for u in sys.argv[1:]:
    try:
        h=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA,'Accept-Language':'nl'}),timeout=60).read()
    except Exception as e:
        print("ERR",u,e); continue
    s=BeautifulSoup(h,'lxml')
    for t in s(['script','style','nav','header','footer','noscript']): t.decompose()
    main=s.find('main') or s.body
    txt=main.get_text('\n'); txt=re.sub(r'\n\s*\n+','\n',txt)
    name=re.sub(r'[^a-zA-Z0-9]+','_',u.split('//')[1])[:100]
    open(f"{W}/web/{name}.txt","w").write("URL: "+u+"\n"+txt)
    # links
    links=[(a.get_text(' ',strip=True),a['href']) for a in main.find_all('a',href=True)]
    open(f"{W}/web/{name}.links","w").write("\n".join(f"{t}\t{h}" for t,h in links))
    print(u,len(txt),name)
