import sys,re,html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.o=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style','noscript','template'): s.skip+=1
        if t in('p','br','li','h1','h2','h3','h4','tr','div','section','td','th'): s.o.append('\n')
        if t=='a':
            d=dict(a)
            h=d.get('href','')
            if h.startswith('http') and 'maglr' not in h and 'share' not in h: s.o.append('[[%s]] '%h)
    def handle_endtag(s,t):
        if t in('script','style','noscript','template'): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.o.append(d)
raw=open(sys.argv[1],encoding='utf-8',errors='replace').read()
p=P(); p.feed(raw); t=''.join(p.o); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
# dedupe: cut at 'Deel deze publicatie'
i=t.find('Deel deze publicatie')
print(t[:i] if i>0 else t)
