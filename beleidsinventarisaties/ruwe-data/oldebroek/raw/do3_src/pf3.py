import pdfplumber
pg=pdfplumber.open('pdf/bestuursakkoord_0907.pdf').pages[21]
for w in pg.extract_words():
    if w['text'] in ('Ruimtelijke','Toerisme','Wethouder','Burgemeester','Erik','Martijn','Tom','Wmo','Beheer','Grondbedrijf','Coördinerend','Wonen','Stikstof','Omgevingswet','Buurtmidden','Centrum','ICT','Financiën'):
        print(w['text'],round(w['x0']),round(w['top']))
