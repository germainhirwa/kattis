import sys; from collections import Counter
names = [l.strip().split() for l in sys.stdin]
names.sort(key=lambda x: (x[1], x[0]))
ctr = Counter(l[0] for l in names)
for fi, la in names:
    if ctr[fi] == 1: print(fi)
    else: print(fi, la)