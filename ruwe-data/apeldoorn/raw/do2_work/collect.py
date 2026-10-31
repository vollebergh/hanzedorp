# DO2 Apeldoorn: verzamelt via Open Besluitvorming (bronsleutel apeldoorn) documenten bij provinciale zoektermen (titels/datums); teksten volgen via ori.py get
import json, subprocess, os, sys
ORI='/home/nick/Claude/Hanzedorp/tools/ori.py'
OUT='data/docs'
os.environ['ORI_CACHE']=os.path.abspath('ori')
QUERIES=['"Groene ontwikkelingszone"','"Gelders natuurnetwerk"','"Groene Balans"','weidevogelgebied','ganzenrustgebied','"Nationaal landschap" kernkwaliteiten',
 '"Omgevingsverordening Gelderland"','"artikel 5.64"','"regionale woonafspraken"','"reactie van de provincie"','"provincie Gelderland" vooroverleg',
 'Regisseur Ruimte','BOPA provincie advies instemming','puntenmethode','versterkingsopgave','natte landnatuur','intrekgebied','waterwingebied','grondwaterbeschermingsgebied',
 'stikstofruimte woningbouw','stikstofreductiegebied','"beperkingengebied stikstofemissie"','voorbeschermingsregels','Versnellingsteam','"Wonen op de boerderij"',
 '"collectieve wooninitiatieven"','woondeal Stedendriehoek','Gebiedsagenda Stedendriehoek','netcongestie woningbouw','"netbewust"','Kernkwaliteiten Veluwe',
 '"Veluwe" woningbouw buitengebied','zienswijze provincie omgevingsplan','Matrix provinciale betrokkenheid','"Atelier Gelderland"','Gelders Genootschap ervenconsulent',
 '"Wegingsmodel"','"functieverandering" buitengebied','"Waar de stallen verdwijnen"','"Rood voor Groen"','"rood-voor-rood"','"Gedeputeerde Staten" woningbouw','"Provinciale Staten" Apeldoorn woningbouw buitengebied',
 'ontheffing instructieregel','"artikel 1.6" omgevingsverordening','"instemming" Gedeputeerde Staten woningbouw','plancapaciteit','Stedendriehoek verstedelijkingsstrategie',
 'Omgevingsvisie Gelderland zienswijze','ontwerp-Omgevingsvisie Gelderland','"Gaaf Gelderland"','"Wijziging Omgevingsverordening"','Kayersmolen','Veluwe stikstof vergunning woningbouw',
 'Natura 2000 woningbouw stikstof','"Mooi Veluwe"','Veluweaanpak','VeluweAlliantie','natuurbrand','klimaatadaptatie risicoanalyse']
seen={}
for q in QUERIES:
    p=subprocess.run(['python3','-I',ORI,'--rate','25','search',q,'--org','apeldoorn','--date-from','2020-01-01','--limit','60','--json','--sort','date_desc'],capture_output=True,text=True)
    txt=p.stdout
    try: arr=json.loads(txt[txt.index('['):])
    except Exception as e: print('ERR',q,e,txt[:200],p.stderr[:200]); continue
    n=0
    for d in arr:
        eid=d['entityId']
        if eid not in seen: seen[eid]={'title':d.get('title'),'date':(d.get('sortDate') or '')[:10],'type':d.get('entityType'),'q':[q]}; n+=1
        else: seen[eid]['q'].append(q)
    print(q,len(arr),'nieuw',n,flush=True)
    json.dump(seen,open(OUT+'/_collect_index.json','w'),indent=1,ensure_ascii=False)
print('totaal uniek',len(seen))
