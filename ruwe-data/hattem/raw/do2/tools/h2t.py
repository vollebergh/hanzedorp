"""HTML -> text (strip script/style). Usage: python3 -I h2t.py < in.html"""
import sys,re,html
t=sys.stdin.read()
t=re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>',' ',t,flags=re.S|re.I)
t=re.sub(r'<br\s*/?>|</p>|</li>|</h\d>|</tr>','\n',t,flags=re.I)
t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t)
t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
print(t)
