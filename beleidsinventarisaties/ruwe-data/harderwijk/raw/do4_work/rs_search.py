import json,urllib.request,sys
UA='Mozilla/5.0 (X11; Linux x86_64) Chrome/124.0.0.0'
def q(term,start=0,size=50):
    body={"StartRow":start,"PageSize":size,"ShouldReturnHighlights":True,"ShouldCountFacets":False,"SortOrder":"UitspraakDatumDesc","SearchTerms":[{"Term":term,"Field":"AlleVelden"}],"Contentsoorten":[],"Rechtsgebieden":[],"Instanties":[],"DatumPublicatie":[],"DatumUitspraak":[],"Advanced":{"PublicatieStatus":"AlleenGepubliceerd"},"CorrelationId":"x","Proceduresoorten":[]}
    r=urllib.request.Request('https://uitspraken.rechtspraak.nl/api/zoek',data=json.dumps(body).encode(),headers={'User-Agent':UA,'Content-Type':'application/json'})
    return json.load(urllib.request.urlopen(r,timeout=60))
seen={}
terms=sys.argv[1:]
for t in terms:
    d=q(t)
    print('###',t,d.get('NumFound') or d.get('Count') or len(d['Results']), list(d.keys())[:6])
    for x in d['Results']:
        e=x['TitelEmphasis']
        if e in seen: continue
        seen[e]=x
        print(x['Uitspraakdatum'],'|',e,'|',x['Titel'][:60],'|',x['Tekstfragment'][:230].replace('\n',' '))
json.dump(seen,open('rs_seen.json','w'))
