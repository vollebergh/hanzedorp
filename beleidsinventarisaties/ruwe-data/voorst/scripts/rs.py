import sys,json,urllib.request
def search(term,start=0,size=50,order="UitspraakDatumDesc"):
    body={"StartRow":start,"PageSize":size,"ShouldReturnHighlights":True,"ShouldCountFacets":False,"SortOrder":order,"SearchTerms":[{"Term":term,"Field":"AlleVelden"}],"Contentsoorten":[],"Rechtsgebieden":[],"Instanties":[],"DatumPublicatie":[],"DatumUitspraak":[],"Advanced":{"PublicatieStatus":"AlleenGepubliceerd"},"CorrelationId":"x","Proceduresoorten":[]}
    req=urllib.request.Request('https://uitspraken.rechtspraak.nl/api/zoek',data=json.dumps(body).encode(),headers={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) Chrome/130'})
    return json.load(urllib.request.urlopen(req,timeout=60))
if __name__=='__main__':
    for term in sys.argv[1:]:
        r=search(term)
        print('##',term,r['ResultCount'])
        for x in r['Results']:
            print(' ',x['TitelEmphasis'],'|',x['Uitspraakdatum'],'|',x['Titel'][:60],'|',x['Tekstfragment'][:260].replace('\n',' '))
