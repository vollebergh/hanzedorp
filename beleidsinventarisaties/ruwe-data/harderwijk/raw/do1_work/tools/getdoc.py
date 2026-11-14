# gebruik: getdoc.py <doc-id> ...  -> pdf/<id>.bin + pdf/<id>.txt  (PDF via pdfplumber, DOCX via zip/xml)
import sys,os,subprocess,re,zipfile
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get(i):
    b=f"{W}/pdf/{i}.bin"; txt=f"{W}/pdf/{i}.txt"
    if os.path.exists(txt) and os.path.getsize(txt)>0: return txt
    subprocess.run(["curl","-s","-L","-A","Mozilla/5.0 (X11; Linux x86_64) Chrome/120","-o",b,f"https://api1.ibabs.eu/publicdownload.aspx?site=Harderwijk&id={i}"],check=True)
    head=open(b,'rb').read(8); out=""
    if head.startswith(b'%PDF'):
        import pdfplumber
        with pdfplumber.open(b) as p:
            for n,pg in enumerate(p.pages,1):
                out+=f"\n=== p.{n} ===\n"+(pg.extract_text() or "")
    elif head.startswith(b'PK'):
        z=zipfile.ZipFile(b)
        x=z.read('word/document.xml').decode('utf8','ignore')
        x=re.sub(r'</w:p>','\n',x); x=re.sub(r'<w:tab/>','\t',x); x=re.sub(r'<[^>]+>','',x)
        import html; out=html.unescape(x)
    else:
        out="NIET-PDF/DOCX: "+repr(head)
    open(txt,"w").write(out); return txt
for i in sys.argv[1:]:
    t=get(i); print(t, len(open(t).read()))
