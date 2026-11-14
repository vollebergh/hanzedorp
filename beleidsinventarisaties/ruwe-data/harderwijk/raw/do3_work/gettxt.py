import sys,re,html
t=open(sys.argv[1],errors='replace').read()
m=re.search(r'<main.*?</main>',t,re.S)
t=m.group(0) if m else t
t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
t=re.sub(r'</(p|h\d|li|div|tr)>','\n',t)
t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
print(t.strip())
