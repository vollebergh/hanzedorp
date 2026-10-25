import sys,urllib.request,urllib.parse,re,html,http.cookiejar
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders=[('User-Agent','Mozilla/5.0')]
base='https://olstwijhe.bestuurlijkeinformatie.nl'
x=op.open(base+'/Search').read().decode()
f=re.search(r'<form method="post"[^>]*id="search-form".*?</form>',x,re.S).group(0)
data={}
for m in re.finditer(r'<input[^>]*>',f):
    n=re.search(r'name="([^"]+)"',m.group(0)); v=re.search(r'value="([^"]*)"',m.group(0)); t=re.search(r'type="([^"]+)"',m.group(0))
    if n and (not t or t.group(1) not in ('checkbox','radio')): data[n.group(1)]=html.unescape(v.group(1)) if v else ''
data['Query']=sys.argv[1]
r=op.open(urllib.request.Request(base+'/Search/Results',data=urllib.parse.urlencode(data).encode(),headers={'X-Requested-With':'XMLHttpRequest'})).read().decode()
open('ibs_last.html','w').write(r)
for m in re.finditer(r'href="([^"]+)"[^>]*>(.*?)</a>',r,re.S):
    t=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',m.group(2)))).strip()
    if t: print(m.group(1),'|',t[:160])
