# column-aware extraction: split each page into N vertical columns by detecting gaps in word x-positions
import sys,pdfplumber
src,dst=sys.argv[1],sys.argv[2]
out=[]
with pdfplumber.open(src) as pdf:
    for i,p in enumerate(pdf.pages):
        words=p.extract_words()
        W=p.width
        # histogram of x coverage
        bins=[0]*int(W+1)
        for w in words:
            for x in range(int(w['x0']),int(w['x1'])+1):
                if x<len(bins): bins[x]+=1
        # find gaps >= 12pt with zero coverage inside text area
        xs=[w['x0'] for w in words]
        if not xs: out.append(f"\n=== p.{i+1} ===\n"); continue
        lo,hi=int(min(xs)),int(max(w['x1'] for w in words))
        cuts=[];run=0
        for x in range(lo,hi):
            if bins[x]==0: run+=1
            else:
                if run>=12: cuts.append(x-run//2)
                run=0
        edges=[0]+cuts+[W]
        txt=[]
        for a,b in zip(edges,edges[1:]):
            c=p.crop((a,0,b,p.height))
            t=c.extract_text() or ''
            if t.strip(): txt.append(t)
        out.append(f"\n=== p.{i+1} ===\n"+"\n---col---\n".join(txt))
open(dst,'w').write(''.join(out))
