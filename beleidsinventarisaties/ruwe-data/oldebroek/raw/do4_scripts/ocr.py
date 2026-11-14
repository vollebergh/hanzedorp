import sys,glob
from rapidocr_onnxruntime import RapidOCR
eng=RapidOCR()
out=[]
for f in sorted(glob.glob(sys.argv[1]+'/p*.png')):
    res,_=eng(f)
    lines=[]
    if res:
        # sort by y then x roughly
        res=sorted(res,key=lambda r:(round(r[0][0][1]/12),r[0][0][0]))
        lines=[r[1] for r in res]
    out.append(f'\n=== {f.split("/")[-1]} ===\n'+'\n'.join(lines))
open(sys.argv[2],'w').write(''.join(out)); print('done')
