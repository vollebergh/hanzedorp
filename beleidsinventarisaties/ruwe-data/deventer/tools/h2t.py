import sys,re,html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.o=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style'): s.skip+=1
        if t in('p','div','br','tr','li','h1','h2','h3','h4','h5','table','dt','dd'): s.o.append('\n')
        if t in('td','th'): s.o.append(' | ')
    def handle_endtag(s,t):
        if t in('script','style'): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.o.append(d)
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
p=P(); p.feed(t); x=''.join(p.o)
x=re.sub(r'[ \t\xa0]+',' ',x); x=re.sub(r'\n\s*\n+','\n\n',x)
print(x)
