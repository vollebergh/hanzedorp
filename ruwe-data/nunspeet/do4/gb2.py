import gb,json
allr=[]
for yr in ['2024','2025','2026']:
    for part in [(f'{yr}-01-01',f'{yr}-04-30'),(f'{yr}-05-01',f'{yr}-08-31'),(f'{yr}-09-01',f'{yr}-12-31')]:
        qq=f'dt.creator="Nunspeet" AND dt.type=="gemeenteblad" AND dt.modified>={part[0]} AND dt.modified<={part[1]}'
        try:
            tot,o=gb.q(qq,100)
        except Exception as e:
            print('ERR',part,e); continue
        print(part,tot,len(o))
        allr+=o
json.dump(allr,open('gmb_all.json','w'),ensure_ascii=False)
