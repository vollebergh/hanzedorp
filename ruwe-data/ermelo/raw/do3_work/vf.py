import sys,re
sys.path.insert(0,'.')
from fetch import html2text
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
x=html2text(t); x=re.sub(r'\n\s*\n+','\n',x)
x=re.sub(r'(\n[ -]*)+\n','\n',x)
i=x.find(sys.argv[2]) if len(sys.argv)>2 else 0
i=max(i,0)
print(x[i:i+int(sys.argv[3]) if len(sys.argv)>3 else i+4000])
