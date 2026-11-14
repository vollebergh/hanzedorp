import sys,re,json,http.cookiejar,urllib.request,urllib.parse
rid=sys.argv[1]; out=sys.argv[2]
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); op.addheaders=[('User-Agent','Mozilla/5.0')]
h=op.open('https://olstwijhe.bestuurlijkeinformatie.nl/Reports/Details/'+rid).read().decode()
tok=re.search(r'name="__RequestVerificationToken" type="hidden" value="([^"]+)"',h)
cols=json.loads(re.search(r"data-columns='([^']+)'",h).group(1))
d={'draw':'1','start':'0','length':'2000','search[value]':'','search[regex]':'false','order[0][column]':'1','order[0][dir]':'desc'}
for i,c in enumerate(cols):
    d[f'columns[{i}][data]']=c['data']; d[f'columns[{i}][name]']=c['name']; d[f'columns[{i}][searchable]']='true'; d[f'columns[{i}][orderable]']='true'; d[f'columns[{i}][search][value]']=''; d[f'columns[{i}][search][regex]']='false'
hd={'X-Requested-With':'XMLHttpRequest'}
if tok: d['__RequestVerificationToken']=tok.group(1); hd['RequestVerificationToken']=tok.group(1)
r=op.open(urllib.request.Request('https://olstwijhe.bestuurlijkeinformatie.nl/Reports/GetReportData/'+rid,data=urllib.parse.urlencode(d).encode(),headers=hd)).read().decode()
open(out,'w').write(r)
j=json.loads(r); print(j.get('recordsTotal'), len(j.get('data',[])))
