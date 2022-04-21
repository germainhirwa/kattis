from collections import deque
import sys

v, e = map(int, input().split())
names = list(input().split())
g = {'English': {}}

for n in names:
    g[n] = {}

for line in sys.stdin:
    a, b, w = line.split()
    g[a][b] = g[b][a] = int(w)

D = dict(map(lambda x: (x, (float('inf'), float('inf'), None)), g.keys()))
D['English'] = (0, 0, None)
q = deque([(0, 0, 'English')])

while q:
    pp, dd, uu = q.popleft()
    for nn in g[uu]:
        if (pp + 1 < D[nn][0]) or (pp + 1 == D[nn][0] and g[uu][nn] <= g[D[nn][2]][nn]):
            D[nn] = (pp + 1, dd + g[uu][nn], uu)
            q.append((pp + 1, dd + g[uu][nn], nn))

g[None] = {}
g['English'][None] = g[None]['English'] = 0
if (float('inf'), float('inf')) in map(lambda x: x[:2], D.values()):
    print('Impossible')
else:
    print(sum(map(lambda x: g[D[x[0]][-1]][x[0]], D.items())))