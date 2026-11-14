import sys,json,urllib.request,urllib.parse,re,html
# usage: wpfull.py site slug  -> prints date,title,content text
site=sys.argv[1]; slug=sys.argv[2]
url=f"https://{site}/wp-json/wp/v2/posts?"+urllib.parse.urlencode({'slug':slug,'_fields':'date,modified,link,title,content,author'})
data=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60))
for p in data:
    c=p['content']['rendered']
    c=re.sub(r'<br\s*/?>|</p>|</li>|</h\d>','\n',c); c=re.sub(r'<[^>]+>','',c); c=html.unescape(c); c=re.sub(r'\n\s*\n+','\n',c)
    print('DATE',p['date'],'MOD',p['modified']); print('TITLE',html.unescape(p['title']['rendered'])); print('URL',p['link']); print(c.strip())
