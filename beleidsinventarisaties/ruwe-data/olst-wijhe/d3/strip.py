import sys,re,html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style','noscript','svg'): s.skip+=1
        if t in('p','br','div','li','h1','h2','h3','h4','h5','tr','td','th','section','article','time','span') : s.out.append('\n' if t!='span' else ' ')
        if t=='time':
            d=dict(a).get('datetime');
            if d: s.out.append('[time:'+d+'] ')
        if t=='meta':
            pass
    def handle_startendtag(s,t,a):
        if t=='meta':
            d=dict(a)
            if d.get('property','') in('article:published_time','article:modified_time','og:title') or d.get('name','') in ('date','DCTERMS.issued','DCTERMS.modified','dcterms.issued','dcterms.modified','description'):
                s.out.append('\n[meta %s=%s]\n'%(d.get('property') or d.get('name'), d.get('content')))
    def handle_endtag(s,t):
        if t in('script','style','noscript','svg'): s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
raw=open(sys.argv[1],'rb').read().decode('utf-8','replace')
p=P();p.feed(raw)
t=''.join(p.out)
t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
print(t)
