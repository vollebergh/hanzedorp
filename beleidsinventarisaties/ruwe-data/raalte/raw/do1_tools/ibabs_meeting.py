import re,html,sys
s=open(sys.argv[1],encoding='utf-8').read()
# agenda items and documents
for m in re.finditer(r'(<div[^>]*class="[^"]*agenda-item[^"]*"|href="(/Agenda/Document/[^"]+)"[^>]*>(.*?)</a>|<h[2-5][^>]*>(.*?)</h[2-5]>)',s,re.S):
    if m.group(2):
        t=re.sub(r'<[^>]+>',' ',m.group(3)); t=re.sub(r'\s+',' ',html.unescape(t)).strip()
        print('   DOC',t,'|',html.unescape(m.group(2)))
    elif m.group(4):
        t=re.sub(r'<[^>]+>',' ',m.group(4)); t=re.sub(r'\s+',' ',html.unescape(t)).strip()
        if t: print('ITEM',t)
