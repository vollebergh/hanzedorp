import sys,re
for fn in sys.argv[1:]:
    t=open(fn).read()
    body,_,links=t.partition('\n\nLINKS:\n')
    i=body.find('Over deze website'); 
    j=body.find('Deel deze pagina')
    if j<0: j=body.find('Bezoekadres\nMarkt 1')
    main=body[i+len('Over deze website'):j] if i>=0 else body[:j]
    main='\n'.join(l.strip() for l in main.split('\n') if l.strip())
    print('#####',fn,'\n',main)
    L=[l for l in links.split('\n') if re.search(r'(\.pdf|/Docs/|/Document|/Bestanden|download|bestuurlijkeinformatie|officielebekendmakingen|ruimtelijkeplannen|omgevingswet)',l,re.I)]
    print('-- doclinks:', '\n'.join(sorted(set(L))))
