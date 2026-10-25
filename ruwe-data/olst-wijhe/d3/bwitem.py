import re,sys
t=open('bw.txt').read()
parts=re.split(r'\n(?====== \[)',t)
for arg in sys.argv[1:]:
    idx,num=arg.split(':')
    p=[x for x in parts if x.startswith(f'===== [{idx}]')][0]
    items=re.split(r'\n(?=\d\d\. )',p)
    for it in items:
        if it.startswith(num+'. '):
            print(p.split('\n')[0]); print(it.split('ATT:')[0]); print('-----')
