import sys,urllib.request,re,html
for id in sys.argv[1:]:
    u=f'https://zoek.officielebekendmakingen.nl/{id}.html'
    x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode('utf-8','replace')
    m=re.search(r'<div[^>]*id="broodtekst"[^>]*>(.*?)</div>\s*</div>\s*</div>',x,re.S) or re.search(r'<main.*?</main>',x,re.S)
    t=m.group(0) if m else x
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    t=re.sub(r'<(br|/p|/li|/h\d|/tr|/div)[^>]*>','\n',t); t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
    t=re.sub(r'\n\s*\n+','\n',t)
    print('=====',u); print(t.strip()[:6000])
