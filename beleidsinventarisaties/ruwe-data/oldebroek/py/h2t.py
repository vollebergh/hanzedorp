import sys,re
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style','noscript'): s.skip+=1
        if t in('p','br','li','h1','h2','h3','h4','tr','div','section'): s.out.append('\n')
        if t=='a':
            d=dict(a)
            if d.get('href') and not d['href'].startswith('#') and not d['href'].startswith('mailto'): s.out.append('[[%s]] '%d['href'])
            elif d.get('href','').startswith('mailto'): s.out.append('[[mailto:'+d['href'][7:40]+']] ')
    def handle_endtag(s,t):
        if t in('script','style','noscript'): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
raw=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'<div[^>]*class="[^"]*main-content[^"]*"',raw)
if m: raw=raw[m.start():]
e=raw.find('id="content-footer"')
if e>0: raw=raw[:e]
p=P(); p.feed(raw)
t=''.join(p.out); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
print(t)
