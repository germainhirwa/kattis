import sys
v, e = map(int, input().split())
di, do = [0]*v, [0]*v
for l in sys.stdin:
    a, b = map(int, l.split())
    a -= 1; b -= 1
    di[b] += 1; do[a] += 1
oi1, io1, eq = [], [], []
for i in range(v):
    if di[i] - do[i] in [-1, 0, 1]: [eq, io1, oi1][di[i] - do[i]].append(i)
if len(oi1) > 1 or len(io1) > 1 or len(oi1) + len(io1) + len(eq) != v: print('no')
elif oi1: print(oi1[0]+1, io1[0]+1)
else: print('anywhere')