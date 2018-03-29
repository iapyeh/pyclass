import sys,os,re
path = 'filelist.txt'
fd = open(path)
data = {}
target = sys.argv[1].lower()
digits = re.compile('\D(\d+)(\D?.*)')
count = 0
for line in fd:
    line = line.strip()
    if not line: continue
    count += 1
    basename = os.path.splitext(line.split('\\')[-1])[0]
    if basename.find(target)==-1: continue
    m = digits.search(basename)
    d = m.group(1)
    if d.startswith('1'):
        year = int(d[:3])
        subcode = d[3:]+m.group(2)
    else:
        year = int(d[:2])
        subcode = d[2:]+m.group(2)
    try:
        data[year].append(subcode)
    except KeyError:
        data[year] = [subcode]

years = data.keys()
years.sort()
total = 0
for year in years:
    print
    print year, 'total',len(data[year])
    print data[year]
    total += len(data[year])
print 'total',total, 'out of', count