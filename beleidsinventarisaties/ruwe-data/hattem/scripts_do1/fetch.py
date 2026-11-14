import sys, subprocess, re, html, os
from html.parser import HTMLParser
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0; s.links=[]
    def handle_starttag(s,t,a):
        if t in('script','style','noscript','svg'): s.skip+=1
        if t in('p','br','div','li','h1','h2','h3','h4','tr','section'): s.out.append('\n')
        if t=='a':
            d=dict(a); h=d.get('href')
            if h: s.links.append(h)
    def handle_endtag(s,t):
        if t in('script','style','noscript','svg'): s.skip=max(0,s.skip-1)
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
url, out = sys.argv[1], sys.argv[2]
raw=subprocess.run(['curl','-s','-L','-A',UA,'--max-time','60',url],capture_output=True).stdout
if raw[:4]==b'%PDF':
    open(out+'.pdf','wb').write(raw); print('PDF saved',out+'.pdf',len(raw)); sys.exit()
t=raw.decode('utf-8','replace')
p=P(); p.feed(t)
txt=re.sub(r'\n\s*\n+','\n',''.join(p.out))
txt=re.sub(r'[ \t]+',' ',txt)
open(out,'w').write(url+'\n'+txt+'\n\nLINKS:\n'+'\n'.join(p.links))
print(len(txt))
