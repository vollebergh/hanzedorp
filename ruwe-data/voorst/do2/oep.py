"""Zoek in officielebekendmakingen via SRU (repository.overheid.nl). python3 -I oep.py '<cql>' [max] [start]"""
import sys, urllib.request, urllib.parse, xml.etree.ElementTree as ET
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
ns={'s':'http://docs.oasis-open.org/ns/search-ws/sruResponse','d':'http://purl.org/dc/terms/'}
def run(q, n=50, start=1, show=True):
    p=urllib.parse.urlencode({'version':'1.2','operation':'searchRetrieve','x-connection':'oep','query':q,'maximumRecords':n,'startRecord':start})
    x=ET.fromstring(urllib.request.urlopen(urllib.request.Request('https://repository.overheid.nl/sru?'+p,headers={'User-Agent':UA}),timeout=90).read())
    tot=x.find('s:numberOfRecords',ns)
    out=[]
    for r in x.findall('.//s:record',ns):
        g=lambda path:(r.find(path,ns).text if r.find(path,ns) is not None else '')
        out.append((g('.//d:modified'), g('.//d:creator'), g('.//d:title')[:150], g('.//d:identifier')))
    if show:
        print('TOTAL', tot.text if tot is not None else '?')
        for o in out: print(' | '.join(o))
    return out
if __name__=='__main__':
    run(sys.argv[1], int(sys.argv[2]) if len(sys.argv)>2 else 50, int(sys.argv[3]) if len(sys.argv)>3 else 1)
