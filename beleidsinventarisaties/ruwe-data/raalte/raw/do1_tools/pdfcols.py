import sys, pdfplumber
f=sys.argv[1]; pages=[int(x) for x in sys.argv[2].split(',')]
with pdfplumber.open(f) as p:
    for n in pages:
        pg=p.pages[n-1]; w=pg.width
        for name,box in (('LEFT',(0,0,w/2,pg.height)),('RIGHT',(w/2,0,w,pg.height))):
            print(f'=== p.{n} {name}'); print(pg.crop(box).extract_text())
