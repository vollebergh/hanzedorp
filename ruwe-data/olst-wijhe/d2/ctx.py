import sys,re
f=sys.argv[1]; lines=open(f,encoding='utf8',errors='ignore').read().split('\n')
for ln in map(int,sys.argv[2:]):
    i=ln-1; hdr=None; item=None
    j=i
    while j>=0:
        if item is None and (lines[j].startswith('### ') or re.match(r'^\d+\. ',lines[j])): item=lines[j]
        if lines[j].startswith('########') : hdr=lines[j]; break
        j-=1
    print(f"--- line {ln} | {hdr[:90] if hdr else None} | {item[:200] if item else None}")
    for k in range(max(0,i-6),min(len(lines),i+3)): print('   ',lines[k][:420])
