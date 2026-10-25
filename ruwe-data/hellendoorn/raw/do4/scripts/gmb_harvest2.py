import urllib.request, urllib.parse, re, sys, time
# usage: gmb_harvest2.py out.tsv 'query'  (pages of 250, retries, appends incrementally)
out = sys.argv[1]; q = sys.argv[2]
start = 1; n = None
f = open(out, 'w')
while True:
    url = "https://repository.overheid.nl/sru?" + urllib.parse.urlencode({'operation': 'searchRetrieve', 'version': '2.0', 'x-connection': 'officielepublicaties', 'maximumRecords': '250', 'startRecord': str(start), 'query': q})
    for attempt in range(6):
        try:
            d = urllib.request.urlopen(url, timeout=180).read().decode()
            break
        except Exception as e:
            print('retry', start, e, file=sys.stderr); time.sleep(5 * (attempt + 1))
    else:
        print('FAILED at', start, file=sys.stderr); break
    n = int(re.findall(r'numberOfRecords>(\d+)<', d)[0])
    recs = re.findall(r'<sru:record>.*?</sru:record>', d, re.S)
    for r in recs:
        g = lambda t: (re.findall(r'<dcterms:' + t + r'[^>]*>(.*?)</dcterms:' + t + '>', r, re.S) or [''])[0].replace('\t', ' ').replace('\n', ' ')
        f.write('\t'.join([g('identifier'), g('date'), g('type'), g('creator'), g('title')]) + '\n')
    f.flush()
    start += len(recs)
    print(start, n, file=sys.stderr)
    if not recs or start > n: break
f.close()
print(n)
