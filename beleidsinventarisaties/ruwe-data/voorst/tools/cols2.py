import sys, pdfplumber
def columns(p, mingap=7):
    words=p.extract_words(use_text_flow=False, keep_blank_chars=False)
    W=int(p.width)
    cov=[0]*(W+2)
    for w in words:
        for x in range(int(w['x0']),int(w['x1'])+1):
            if 0<=x<=W: cov[x]+=1
    # find gaps
    gaps=[];start=None
    for x in range(0,W+1):
        if cov[x]==0:
            if start is None: start=x
        else:
            if start is not None:
                if x-start>=mingap and start>20: gaps.append((start,x))
                start=None
    cuts=[ (a+b)/2 for a,b in gaps]
    return [0]+cuts+[p.width]
def page_text(p):
    cuts=columns(p)
    out=[]
    for i in range(len(cuts)-1):
        c=p.crop((cuts[i],0,cuts[i+1],p.height))
        t=c.extract_text() or ''
        if t.strip(): out.append(t)
    return '\n\n'.join(out)
if __name__=='__main__':
    src=sys.argv[1]; pages=sys.argv[2]
    with pdfplumber.open(src) as pdf:
        if pages=='all': pl=range(1,len(pdf.pages)+1)
        else:
            pl=[]
            for part in pages.split(','):
                if '-' in part: a,b=part.split('-'); pl+=list(range(int(a),int(b)+1))
                else: pl.append(int(part))
        for n in pl:
            print(f"\n######## PAGE {n}\n"+page_text(pdf.pages[n-1]))
