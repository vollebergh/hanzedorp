# DO2 Ermelo: alle BAG-verblijfsobjecten (woonfunctie, in gebruik) in bbox Ermelo
import json, urllib.request, urllib.parse
BB="166500,478500,178500,489000,EPSG:28992"
feats=[]; start=0
while True:
    q={"service":"WFS","version":"2.0.0","request":"GetFeature","typeNames":"bag:verblijfsobject","outputFormat":"application/json","srsName":"EPSG:28992","bbox":BB,"count":"1000","startIndex":str(start)}
    u="https://service.pdok.nl/lv/bag/wfs/v2_0?"+urllib.parse.urlencode(q)
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=180))
    fs=d.get('features',[]); feats+=fs; print(start,len(fs),flush=True)
    if len(fs)<1000: break
    start+=1000
json.dump({"type":"FeatureCollection","features":feats},open('data/pdok/bag_vbo.json','w'))
print('totaal',len(feats))
