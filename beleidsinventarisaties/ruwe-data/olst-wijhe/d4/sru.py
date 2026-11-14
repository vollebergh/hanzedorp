import re,sys,subprocess
q=sys.argv[1]
out=subprocess.run(['curl','-s','-G','https://zoekservice.overheid.nl/sru/Search','--data-urlencode','x-connection=cvdr','--data-urlencode','operation=searchRetrieve','--data-urlencode','version=1.2','--data-urlencode','query='+q,'--data-urlencode','maximumRecords=200'],capture_output=True,text=True).stdout
print('N=',(re.search(r'numberOfRecords>(\d*)',out) or [0,'?'])[1], re.findall(r'<message>([^<]*)',out))
seen=set()
for r in out.split('<record>')[1:]:
    g=lambda tag: (re.search(r'<'+tag+r'[^>]*>(.*?)</'+tag+'>',r,re.S) or [None,''])[1]
    k=g('dcterms:identifier')
    print(' ',k,'|',g('dcterms:creator'),'|',g('dcterms:issued'),'| uit:',g('overheidrg:uitwerkingtredingDatum'),'|',g('dcterms:title')[:110])
