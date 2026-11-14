import sys,re
for p in sys.argv[1:]:
    t=open(p,encoding='utf8',errors='ignore').read()
    title=t.strip().split('\n')[0]
    i=t.rfind('Over deze website'); j=t.find(' Deel deze pagina',i)
    body=t[i+len('Over deze website'):j] if i>=0 and j>i else t[:3000]
    open(p.replace('.txt','.main.txt'),'w').write(title+'\n'+body)
