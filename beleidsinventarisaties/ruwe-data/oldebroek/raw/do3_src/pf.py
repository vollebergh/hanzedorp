import pdfplumber
p=pdfplumber.open('pdf/bestuursakkoord_0907.pdf')
pg=p.pages[21]
print(pg.width,pg.height)
ws=pg.extract_words()
# columns by x0
xs=sorted(set(round(w['x0']) for w in ws))
print(xs[:60])
for name,(a,b) in {'left':(0,pg.width/2),'right':(pg.width/2,pg.width)}.items():
    c=pg.crop((a,0,b,pg.height))
    print('-----',name); print(c.extract_text())
