import sys,re,html
sys.path.insert(0,'.')
from fetch import html2text
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
# try article tag, else full
m=re.search(r'<article.*?</article>',t,re.S)
b=m.group(0) if m else t
x=html2text(b)
x=re.sub(r'\n\s*\n+','\n',x)
print(x[:int(sys.argv[2]) if len(sys.argv)>2 else 6000])
