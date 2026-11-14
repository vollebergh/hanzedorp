import sys,json,urllib.request,urllib.parse,re,html
# usage: wp.py site "search terms" [after=YYYY-MM-DD] [per_page]
site=sys.argv[1]; q=sys.argv[2]; after=sys.argv[3] if len(sys.argv)>3 else '2024-01-01'
pp=sys.argv[4] if len(sys.argv)>4 else '50'
params={'per_page':pp,'after':after+'T00:00:00','_fields':'id,date,link,title'}
if q: params['search']=q
url=f"https://{site}/wp-json/wp/v2/posts?"+urllib.parse.urlencode(params)
req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
try:
    data=json.load(urllib.request.urlopen(req,timeout=60))
except Exception as e:
    print('ERR',e,url); sys.exit()
for p in data:
    print(p['date'][:10], html.unescape(re.sub('<[^>]+>','',p['title']['rendered'])), p['link'])
