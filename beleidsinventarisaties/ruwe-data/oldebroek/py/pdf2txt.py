import sys,pdfplumber
with pdfplumber.open(sys.argv[1]) as pdf:
    for i,p in enumerate(pdf.pages):
        print(f'\n=== p{i+1} ===')
        print(p.extract_text() or '')
