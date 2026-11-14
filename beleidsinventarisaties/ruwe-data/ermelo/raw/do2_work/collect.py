# DO2 Ermelo: verzamelt via Open Besluitvorming (bronsleutel ermelo) documenten bij provinciale zoektermen (titels/datums; teksten volgen via ori.py get)
import json, subprocess, os, sys
ORI='/home/nick/Claude/Hanzedorp/tools/ori.py'
OUT='data/docs'
os.environ['ORI_CACHE']=os.path.abspath('ori')
QUERIES=['"Groene ontwikkelingszone"','"Gelders natuurnetwerk"','weidevogelgebied','ganzenrustgebied','"Nationaal landschap" kernkwaliteiten',
 '"Omgevingsverordening Gelderland"','"artikel 5.64"','"regionale woonafspraken"','"Natura 2000" vergunning provincie woningbouw','"reactie van de provincie"',
 '"provincie Gelderland" vooroverleg','Regisseur','BOPA provincie advies','puntenmethode','versterkingsopgave','natte landnatuur','intrekgebied','waterwingebied',
 'stikstofruimte woningbouw','stikstofbank','ervenconsulent','functieverandering woningen buitengebied','"Structuurvisie Functieverandering"','Routeboek','"Gebiedsvisie Speuld"',
 '"Garderenseweg 60"','"Zandkampweg 21"','Leuvenumseveld','Riebroekseweg','"stikstofreductiegebied"','"beperkingengebied stikstofemissie"','"voorbeschermingsregels"',
 'Versnellingsteam','"Wonen op de boerderij"','"collectieve wooninitiatieven"','woondeal','Gebiedsagenda','"Ermelo-Harderwijk"','netcongestie','"netbewust"','Kernkwaliteiten',
 '"Veluwe" woningbouw buitengebied','"Provinciale Staten"','"Gedeputeerde Staten"','zienswijze provincie omgevingsplan','Matrix provinciale betrokkenheid','"Atelier Gelderland"','Gelders Genootschap']
seen={}
for q in QUERIES:
    p=subprocess.run(['python3','-I',ORI,'--rate','30','search',q,'--org','ermelo','--date-from','2020-01-01','--limit','60','--json','--sort','date_desc'],capture_output=True,text=True)
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
