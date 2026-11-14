import re,sys,html,subprocess
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
u=sys.argv[1]
t=subprocess.run(['curl','-s','-L','--max-time','40','-A',UA,'https://www.omroepgelderland.nl'+u],capture_output=True).stdout.decode('utf8','ignore')
open('og_'+u.split('/')[2]+'.html','w').write(t)
t=re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>','',t,flags=re.S)
m=re.search(r'<h1.*?(?=Meer nieuws|Lees ook|Gerelateerd|</article>)',t,flags=re.S)
t=m.group(0) if m else t
t=re.sub(r'</(p|div|li|h\d|tr|br)>','\n',t); t=re.sub(r'<[^>]+>','',t); t=html.unescape(t); t=re.sub(r'\n\s*\n+','\n',t)
print(t.strip()[:6000])
