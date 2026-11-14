import urllib.request, json, sys
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
W='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do2/'
URL="https://service.pdok.nl/rvo/brpgewaspercelen/wfs/v1_0?service=WFS&version=2.0.0&request=GetFeature&typeNames=brpgewaspercelen:BrpGewas&outputFormat=application/json&srsName=urn:ogc:def:crs:EPSG::28992&count=1000&bbox=%s,urn:ogc:def:crs:EPSG::28992"
feats={}
def get(x0,y0,x1,y1,depth=0):
    u=URL%f"{x0},{y0},{x1},{y1}"
    r=urllib.request.Request(u,headers={'User-Agent':UA})
    d=json.load(urllib.request.urlopen(r,timeout=180))
    fs=d['features']
    if len(fs)>=1000 and depth<5:
        mx=(x0+x1)/2; my=(y0+y1)/2
        for a,b,c,e in [(x0,y0,mx,my),(mx,y0,x1,my),(x0,my,mx,y1),(mx,my,x1,y1)]:
            get(a,b,c,e,depth+1)
    else:
        if len(fs)>=1000: print('WARN truncated',x0,y0,x1,y1)
        for f in fs: feats[f['id']]=f
x0,y0,x1,y1=193000,485200,206000,497000
step=2000
x=x0
while x<x1:
    y=y0
    while y<y1:
        get(x,y,min(x+step,x1),min(y+step,y1)); y+=step
    x+=step
    print(x,len(feats),flush=True)
json.dump({'type':'FeatureCollection','features':list(feats.values())},open(W+'brp25_heerde_bbox.json','w'))
print('total',len(feats))
