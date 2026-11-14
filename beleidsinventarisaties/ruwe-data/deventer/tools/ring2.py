exec(open('ring.py').read().split("for k,(x,y) in kernen.items():")[0].replace("print(","(lambda *a,**k:None)("))
named={'Stad Deventer/Colmschate/Diepenveen/Schalkhaar (aaneengesloten)':(209072,475001),'Bathmen':(216499,473859),'Lettele':(215431,477000),'Okkenbroek':(218615,479253),'Deventer-zuid (Steenbrugge/Epse-grens?)':(210687,471835)}
for k,(x,y) in named.items():
    u=[p for p in parts if p.distance(Point(x,y))<1][0]
    for r in (250,500,1000):
        ring=u.buffer(r).difference(beb).intersection(gem)
        stat(ring,f'{k} ring {r} m')
