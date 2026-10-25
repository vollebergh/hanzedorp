import sys,re,html
for p in sys.argv[1:]:
    t=open(p,encoding='utf8',errors='ignore').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>|<noscript.*?</noscript>','',t,flags=re.S|re.I)
    t=re.sub(r'<(br|p|div|li|h\d|tr)[^>]*>','\n',t,flags=re.I)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(p.rsplit('.',1)[0]+'.txt','w').write(t)
    print(p,len(t.split()))
