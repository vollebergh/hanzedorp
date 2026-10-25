import sys,re,html,json
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
# try ld+json
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',t,re.S):
    print("LD:",m.group(1)[:1500])
t=re.sub(r'<(script|style)[^>]*>.*?</\1>','',t,flags=re.S)
t=re.sub(r'<[^>]+>','\n',t)
t=html.unescape(t)
t=re.sub(r'\n\s*\n+','\n',t)
print(t[:int(sys.argv[2]) if len(sys.argv)>2 else 6000])
