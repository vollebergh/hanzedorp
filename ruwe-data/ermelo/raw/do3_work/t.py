import sys,re
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/10db2ce5-cf65-46a7-800e-29355f749163/scratchpad/ermelo/raw/do3_work')
from fetch import html2text
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
i=t.find('id="content"'); 
m=re.search(r'<main',t)
b=t[m.start():] if m else t
x=html2text(b)
x=re.sub(r'(\n\s*- ?)+\n','\n',x)
print(x[:int(sys.argv[2]) if len(sys.argv)>2 else 8000])
