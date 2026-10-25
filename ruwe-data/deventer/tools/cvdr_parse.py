import sys, glob, re
import xml.etree.ElementTree as ET
ns={'dcterms':'http://purl.org/dc/terms/','overheid':'http://standaarden.overheid.nl/owms/terms/','overheidrg':'http://standaarden.overheid.nl/cvdr/terms/'}
rows=[]
for f in sorted(glob.glob(sys.argv[1]+'/*.xml')):
    t=ET.parse(f)
    for m in t.iter('{http://standaarden.overheid.nl/cvdr/terms/}meta'):
        g=lambda p: (m.find(p,ns).text if m.find(p,ns) is not None and m.find(p,ns).text else '')
        rows.append((g('.//dcterms:identifier'),g('.//dcterms:creator'),g('.//overheid:isRatifiedBy'),g('.//dcterms:issued'),g('.//overheidrg:inwerkingtredingDatum'),g('.//overheidrg:uitwerkingtredingDatum'),g('.//dcterms:title'),g('.//dcterms:isFormatOf')))
for r in rows: print(' | '.join(r))
