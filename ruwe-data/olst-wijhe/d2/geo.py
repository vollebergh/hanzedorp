import urllib.request,urllib.parse,json,re
A=[('Elshof/Engeweg 10a (Engeweg, 8 woningen)','Engeweg 10a, 8131RP Wijhe'),
('Elshof/Engeweg 8','Engeweg 8, 8131RP Wijhe'),
('Elshof 6c (3 woningen 2022)','Elshof 6c, 8131RR Wijhe'),
('Herxen achter 7a (CPO 3 woningen)','Herxen 7a, 8131PC Wijhe'),
('Herxen 63 (Grolleman 15 woningen)','Herxen 63, 8131PD Wijhe'),
('Marle (Marledijk 33)','Marledijk 33, Marle'),
('Wijhe centrum (Marktstraat 1)','Marktstraat 1, 8131BV Wijhe'),
('Olst centrum (Stationsweg)','Stationsweg 1, Olst'),
('Wesepe kern (Achterhoekstraat)','Achterhoekstraat 1, Wesepe'),
('Boskamp (Hyacintstraat, Klimboom)','Hyacintstraat 1, Olst'),
('Middel/Steunenbergerweg 6','Steunenbergerweg 6, 8121RJ Olst'),
('Boerhaar 43','Boerhaar 43, 8131SV Wijhe'),
('Zandhuisweg 7a','Zandhuisweg 7a, Wijhe'),
('Vettewinkelweg 2','Vettewinkelweg 2, 8131SZ Wijhe'),
('Lierderholthuisweg 3','Lierderholthuisweg 3, 8131PW Wijhe'),
('Welsum Erveweg 8','Erveweg 8, 8196KG Welsum'),
('Wesepe Bokkelerweg 1','Bokkelerweg 1, Wesepe'),
('Den Nul','Nulde 1, Olst'),
('Kloosterhoekweg 3 Welsum','Kloosterhoekweg 3, Welsum'),
('Scholtensweg 50 Wesepe','Scholtensweg 50, Wesepe'),
('Elshagenweg 1 Wesepe','Elshagenweg 1, Wesepe'),
('Kleistraat Olst','Kleistraat 1, Olst'),
('Prinshoeveweg 1','Prinshoeveweg 1, Wijhe'),
]
out=[]
for k,q in A:
    u='https://api.pdok.nl/bzk/locatieserver/search/v3_1/free?'+urllib.parse.urlencode({'q':q,'rows':1,'fl':'weergavenaam,centroide_rd,type','fq':'gemeentenaam:Olst-Wijhe'})
    r=json.load(urllib.request.urlopen(u,timeout=30))['response']['docs']
    if r:
        m=re.match(r'POINT\(([\d.]+) ([\d.]+)\)',r[0]['centroide_rd'])
        out.append((k,r[0]['weergavenaam'],float(m.group(1)),float(m.group(2))))
    else: out.append((k,None,None,None))
for o in out: print(o)
json.dump(out,open('pts_geo.json','w'))
