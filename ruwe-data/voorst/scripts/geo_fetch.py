import urllib.request,urllib.parse,json,sys,os
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) Chrome/130.0.0.0'}
G='geo/'
def get(url,out):
    req=urllib.request.Request(url,headers=UA)
    data=urllib.request.urlopen(req,timeout=180).read()
    open(out,'wb').write(data); return len(data)
# Voorst gemeentegrens PDOK bestuurlijkegebieden OGC API / WFS
u='https://service.pdok.nl/kadaster/bestuurlijkegebieden/wfs/v1_0?'+urllib.parse.urlencode({'service':'WFS','version':'2.0.0','request':'GetFeature','typeNames':'bestuurlijkegebieden:Gemeentegebied','outputFormat':'application/json','srsName':'EPSG:28992','cql_filter':"naam='Voorst'"})
print('gemeente',get(u,G+'gemeente.json'))
d=json.load(open(G+'gemeente.json'))
print(len(d['features']), [f['properties'].get('naam') for f in d['features']], d['features'][0]['properties'])
