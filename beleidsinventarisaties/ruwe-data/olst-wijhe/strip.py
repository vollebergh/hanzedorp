import re,html,sys
x=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'<main.*?</main>',x,re.S) or re.search(r'<article.*?</article>',x,re.S); t=m.group(0) if m else x
if len(sys.argv)>2:
    for a in re.findall(r'href="([^"]+)"',t):
        if re.search(sys.argv[2],a): print('LINK',a)
t=re.sub(r'<script.*?</script>|<style.*?</style>|<nav.*?</nav>','',t,flags=re.S); t=re.sub(r'<(br|/p|/li|/h\d|/div)[^>]*>','\n',t); t=re.sub(r'<[^>]+>','',t); t=html.unescape(t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
print(t)
