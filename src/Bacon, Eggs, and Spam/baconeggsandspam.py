import sys

d = {}

for line in sys.stdin:
    try:
        k = int(line)
        r = sorted(list(d.items()))
        for m,p in r:
            print(m,' '.join(sorted(p)))
        if d:
            print()
        d.clear()
    except:
        q = line.strip().split()
        for f in q[1:]:
            d[f] = d.get(f,[])+[q[0]]