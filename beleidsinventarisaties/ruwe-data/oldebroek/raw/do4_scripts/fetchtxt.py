import sys,re,html,urllib.request
from html.parser import HTMLParser
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style','nav','header','footer'): s.skip+=1
        if t in('p','div','br','tr','li','h1','h2','h3','h4','h5','table'): s.out.append('\n')
        if t in('td','th'): s.out.append(' | ')
    def handle_endtag(s,t):
        if t in('script','style','nav','header','footer'): s.skip=max(0,s.skip-1)
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
url,outp=sys.argv[1],sys.argv[2]
req=urllib.request.Request(url,headers={'User-Agent':UA})
raw=urllib.request.urlopen(req,timeout=90).read().decode('utf-8','replace')
p=P(); p.feed(raw)
t=html.unescape(''.join(p.out))
t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
open(outp,'w').write(t); print(len(t))
