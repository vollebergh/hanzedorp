import re,sys,html,urllib.request,urllib.parse
q=sys.argv[1]
n=int(sys.argv[2]) if len(sys.argv)>2 else 0
url='https://www.bing.com/search?q='+urllib.parse.quote(q)+'&setlang=nl&cc=nl'+(f'&first={n}' if n else '')
req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','Accept-Language':'nl-NL,nl;q=0.9'})
t=urllib.request.urlopen(req,timeout=30).read().decode('utf8','ignore')
for m in re.finditer(r'<li class="b_algo".*?</li>',t,flags=re.S):
    b=m.group(0)
    h=re.search(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',b,flags=re.S)
    s=re.search(r'<p[^>]*>(.*?)</p>',b,flags=re.S)
    link=h.group(1)
    if 'bing.com/ck/a' in link:
        u=re.search(r'[?&]u=a1([^&]+)',link)
        if u:
            import base64
            x=u.group(1); x+='='*(-len(x)%4)
            try: link=base64.urlsafe_b64decode(x).decode()
            except: pass
    print(html.unescape(re.sub('<[^>]+>','',h.group(2))).strip())
    print('  ',link)
    if s: print('  ',html.unescape(re.sub('<[^>]+>','',s.group(1))).strip()[:250])
