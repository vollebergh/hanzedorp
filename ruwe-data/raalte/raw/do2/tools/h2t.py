# HTML -> platte tekst. Gebruik: python3 h2t.py in.html
import sys,re,html
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</li>|</h\d>|</tr>','\n',s)
s=re.sub(r'(?i)</td>|</th>',' | ',s)
s=re.sub(r'<[^>]+>','',s)
s=html.unescape(s)
s=re.sub(r'[ \t\r\f\v]+',' ',s)
print(re.sub(r'\n\s*\n+','\n',s))
