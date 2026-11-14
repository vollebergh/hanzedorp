import pdfplumber
pg=pdfplumber.open('pdf/bestuursakkoord_0907.pdf').pages[21]
ws=pg.extract_words()
for lo,hi in [(600,880),(880,1190)]:
    # lines by top
    sel=[w for w in ws if lo<=w['x0']<hi]
    c=pg.crop((lo,0,hi,pg.height)); print('-----',lo); print(c.extract_text())
