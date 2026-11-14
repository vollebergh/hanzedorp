import sys
for id in sys.argv[1:]:
    s=open(f'{id}.txt').read()
    i=s.find('Delen\n'); j=s.find('Naar boven')
    if i<0: i=0
    print('#######',id); 
    k=s.find('Datum publicatie'); print(' '.join(s[k:k+200].split('\n')[4:12]).replace(' | ',''))
    print(s[i+6:j].strip())
