import re,html,sys,subprocess
def get(n):
    fn=f'cvdr{n}_wti.html'
    subprocess.run(['curl','-s','-L','-A','Mozilla/5.0',f'https://lokaleregelgeving.overheid.nl/CVDR{n}?show-wti=true','-o',fn])
    t=open(fn,encoding='utf-8',errors='replace').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    s=re.sub(r'<[^>]+>','\n',t); s=html.unescape(s); s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    i=s.find('Naar de door u bekeken versie'); j=s.find('Ziet u een fout')
    return s[i:j]
for n in sys.argv[1:]:
    print('=================== CVDR',n)
    print(get(n)[:2500])
