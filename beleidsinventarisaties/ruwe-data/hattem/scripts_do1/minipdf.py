import sys,re,zlib
data=open(sys.argv[1],'rb').read()
out=[]
# build ToUnicode cmaps
streams=[]
for m in re.finditer(rb'stream\r?\n',data):
    s=m.end(); e=data.find(b'endstream',s)
    raw=data[s:e]
    try: dec=zlib.decompress(raw)
    except Exception:
        try: dec=zlib.decompressobj().decompress(raw)
        except Exception: continue
    streams.append(dec)
cmap={}
for d in streams:
    if b'beginbfchar' in d or b'beginbfrange' in d:
        for b in re.finditer(rb'beginbfchar(.*?)endbfchar',d,re.S):
            for a,u in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>',b.group(1)):
                try: cmap[int(a,16)]=bytes.fromhex(u.decode()).decode('utf-16-be','replace')
                except: pass
        for b in re.finditer(rb'beginbfrange(.*?)endbfrange',d,re.S):
            for a,z,u in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>',b.group(1)):
                st=int(u,16)
                for i,c in enumerate(range(int(a,16),int(z,16)+1)): cmap[c]=chr(st+i)
def dhex(h):
    h=h.decode()
    if len(h)%4==0 and cmap:
        return ''.join(cmap.get(int(h[i:i+4],16),'') for i in range(0,len(h),4))
    return ''.join(cmap.get(int(h[i:i+2],16),chr(int(h[i:i+2],16))) for i in range(0,len(h),2))
def dlit(s):
    s=re.sub(rb'\\([nrtbf()\\])',lambda m:{b'n':b'\n',b'r':b'',b't':b' ',b'b':b'',b'f':b'',b'(':b'(',b')':b')',b'\\':b'\\'}[m.group(1)],s)
    s=re.sub(rb'\\(\d{1,3})',lambda m:bytes([int(m.group(1),8)&255]),s)
    if cmap and all(c in cmap for c in s[:5]): return ''.join(cmap.get(c,'') for c in s)
    return s.decode('latin-1')
for d in streams:
    if b'BT' not in d: continue
    for bt in re.finditer(rb'BT(.*?)ET',d,re.S):
        line=[]
        for tok in re.finditer(rb'\[(.*?)\]\s*TJ|\((.*?)(?<!\\)\)\s*Tj|<([0-9A-Fa-f]+)>\s*Tj|(T\*|Td|TD)',bt.group(1),re.S):
            if tok.group(1) is not None:
                for p in re.finditer(rb'\((.*?)(?<!\\)\)|<([0-9A-Fa-f]+)>|(-?\d+\.?\d*)',tok.group(1),re.S):
                    if p.group(1) is not None: line.append(dlit(p.group(1)))
                    elif p.group(2): line.append(dhex(p.group(2)))
                    elif p.group(3) and float(p.group(3))<-200: line.append(' ')
            elif tok.group(2) is not None: line.append(dlit(tok.group(2)))
            elif tok.group(3): line.append(dhex(tok.group(3)))
            else: line.append('\n')
        out.append(''.join(line))
open(sys.argv[2],'w').write('\n'.join(out)); print(len(''.join(out)))
