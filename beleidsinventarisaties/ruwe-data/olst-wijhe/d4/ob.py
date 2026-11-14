import re,html,sys,subprocess
for id in sys.argv[1:]:
    fn=f'{id}.html'
    subprocess.run(['curl','-s','-L','-A','Mozilla/5.0',f'https://zoek.officielebekendmakingen.nl/{id}.html','-o',fn])
    t=open(fn,encoding='utf-8',errors='replace').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    t=re.sub(r'</(p|div|h\d|li|tr|table|dd|dt)>','\n',t); t=re.sub(r'<br\s*/?>','\n',t); t=re.sub(r'</t[dh]>',' | ',t)
    s=re.sub(r'<[^>]+>','',t); s=html.unescape(s); s=re.sub(r'[ \t\r]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    open(f'{id}.txt','w').write(s)
    print(id,len(s))
