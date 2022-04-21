import sys

n = int(input())
d = {}
for line in sys.stdin:
    f, l, c = line.strip().split()
    if c not in d:
        d[c] = {f'{f} {l}'}
    else:
        d[c].add(f'{f} {l}')
r = sorted(map(lambda x: (x[0], len(x[1])), d.items()))
for k, v in r:
    print(k, v)