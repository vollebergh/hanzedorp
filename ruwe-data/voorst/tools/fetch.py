import sys, subprocess, re, os, hashlib
from bs4 import BeautifulSoup
UA=open('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/ua.txt').read().strip()
outdir='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/d1/pg'
os.makedirs(outdir,exist_ok=True)
for url in sys.argv[1:]:
    if not url.startswith('http'): url='https://www.voorst.nl'+url
    name=re.sub(r'[^A-Za-z0-9]+','_',url.replace('https://',''))[:120]
    r=subprocess.run(['curl','-sL','-A',UA,'--max-time','60',url],capture_output=True)
    html=r.stdout.decode('utf8','replace')
    s=BeautifulSoup(html,'html.parser')
    for t in s(['script','style','nav','header','footer','noscript']): t.decompose()
    main=s.find('main') or s.body or s
    txt=main.get_text('\n',strip=True)
    links=[(a.get_text(' ',strip=True),a['href']) for a in main.find_all('a',href=True)]
    p=os.path.join(outdir,name+'.txt')
    with open(p,'w') as f:
        f.write('URL: '+url+'\n\n'+txt+'\n\n--- LINKS ---\n'+'\n'.join(f'{a} | {b}' for a,b in links))
    print(p, len(txt))
