# PDF -> tekst met paginamarkeringen. Gebruik: python3 pdf2txt.py in.pdf out.txt
import sys,pdfplumber
with pdfplumber.open(sys.argv[1]) as p, open(sys.argv[2],'w') as o:
    for i,pg in enumerate(p.pages,1):
        o.write(f'\n=== p.{i} ===\n'+(pg.extract_text() or ''))
