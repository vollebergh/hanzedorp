import sys, re, html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0; s.links=[]
    def handle_starttag(s,t,a):
        if t in ('script','style','noscript','svg'): s.skip+=1
        if t in ('p','br','li','h1','h2','h3','h4','tr','div','section'): s.out.append('\n')
        if t in ('h1','h2','h3','h4'): s.out.append('#'*int(t[1])+' ')
        if t=='li': s.out.append('- ')
        if t=='a':
            d=dict(a); h=d.get('href','')
            if h and not h.startswith('#'): s.links.append(h)
    def handle_endtag(s,t):
        if t in ('script','style','noscript','svg'): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
src=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'<main.*?</main>',src,re.S)
p=P(); p.feed(m.group(0) if m else src)
t=re.sub(r'[ \t]+',' ',''.join(p.out)); t=re.sub(r'\n\s*\n+','\n',t)
print(t.strip())
print('\n--LINKS--')
for l in dict.fromkeys(p.links):
    if re.search(r'\.(pdf|docx?|xlsx?)|bestuurlijkeinformatie|lokaleregelgeving|officielebekendmakingen|ruimtelijkeplannen|omgevingswet|overheid\.nl|/sites/raalte/files',l,re.I): print(l)
