import sys,re,html
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
i=t.find('Geschreven door'); b=t[i:] if i>0 else t
j=b.find('VRMG Shorts'); b=b[:j] if j>0 else b
j=b.find('Mail ons'); b=b[:j] if j>0 else b
b=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>','',b)
b=re.sub(r'(?i)<br\s*/?>|</p>|</li>|</h\d>|</div>','\n',b); b=re.sub(r'<[^>]+>','',b); b=html.unescape(b)
b=re.sub(r'[ \t]+',' ',b)
print(re.sub(r'\n\s*\n+','\n',b)[:6000])
