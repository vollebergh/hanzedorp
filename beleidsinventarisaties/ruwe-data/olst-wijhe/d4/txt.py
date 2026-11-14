import re,html,sys,subprocess
n=sys.argv[1]; url=sys.argv[2] if len(sys.argv)>2 else f'https://lokaleregelgeving.overheid.nl/CVDR{n}'
fn=f'cvdr{n}.html'
subprocess.run(['curl','-s','-L','-A','Mozilla/5.0',url,'-o',fn])
t=open(fn,encoding='utf-8',errors='replace').read()
t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
t=re.sub(r'</(p|div|h\d|li|tr|table)>','\n',t); t=re.sub(r'<br\s*/?>','\n',t); t=re.sub(r'</t[dh]>',' | ',t)
s=re.sub(r'<[^>]+>','',t); s=html.unescape(s); s=re.sub(r'[ \t\r]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
i=s.find('Naar de door u bekeken versie'); j=s.find('Ziet u een fout')
open(f'cvdr{n}.txt','w').write(s[i:j] if i>=0 else s)
print(n, len(s[i:j]))
