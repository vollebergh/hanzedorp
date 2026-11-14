import urllib.request, json
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
W='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/'
u='https://api.pdok.nl/kadaster/bag/ogc/v2/collections/verblijfsobject/items?f=json&limit=1000&bbox=193000,485200,206000,497000&bbox-crs=http://www.opengis.net/def/crs/EPSG/0/28992&crs=http://www.opengis.net/def/crs/EPSG/0/28992'
out=[]
while u:
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=120))
    for f in d['features']:
        p=f['properties']
        out.append({'id':p['identificatie'],'doel':p['gebruiksdoel'],'status':p['status'],'wp':p['woonplaats_naam'],'bron':p['bronhouder_naam'],'x':f['geometry']['coordinates'][0],'y':f['geometry']['coordinates'][1],'opp':p.get('oppervlakte'),'str':p['openbare_ruimte_naam'],'nr':p['huisnummer']})
    nxt=[l['href'] for l in d['links'] if l['rel']=='next']
    u=nxt[0] if nxt and d['features'] else None
    print(len(out),flush=True)
json.dump(out,open(W+'bag_vbo.json','w'))
