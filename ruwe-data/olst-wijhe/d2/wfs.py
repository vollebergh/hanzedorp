import json,urllib.request,urllib.parse,sys
BASE='https://services.geodataoverijssel.nl/geoserver/wfs'
def get(layer,cql,props=None,count=5):
    p={'service':'WFS','version':'2.0.0','request':'GetFeature','typeNames':layer,'outputFormat':'application/json','srsName':'EPSG:28992','count':count,'cql_filter':cql}
    if props: p['propertyName']=props
    u=BASE+'?'+urllib.parse.urlencode(p)
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=90)),u
if __name__=='__main__':
    layer=sys.argv[1]; x,y=sys.argv[2],sys.argv[3]; d=sys.argv[4] if len(sys.argv)>4 else '1'
    r,u=get(layer,f"DWITHIN(SHAPE,POINT({x} {y}),{d},meters)")
    print(u); print(len(r['features'])); 
    for f in r['features']: print(f['properties'])
