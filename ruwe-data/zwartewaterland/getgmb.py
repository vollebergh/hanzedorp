import re,html,sys,requests
UA={'User-Agent':'Mozilla/5.0 Chrome/124'}
def get(idn):
    r=requests.get(f'https://zoek.officielebekendmakingen.nl/{idn}.html',headers=UA,timeout=60)
    s=r.text
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    t=re.sub(r'</(p|div|h\d|li|tr)>','\n',t)
    t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    i=t.find('Gerelateerd')
    return r.status_code,t
if __name__=='__main__':
    for idn in sys.argv[1:]:
        c,t=get(idn)
        open(f'{idn}.txt','w').write(t)
        # print the body part after 'Printen Delen' if present
        j=t.find('Delen')
        print('=====',idn,c,len(t)); print(t[j:j+3500] if j>0 else t[:3500])
