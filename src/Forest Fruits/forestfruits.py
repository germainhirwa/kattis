from heapq import *
import sys

v, e, c, k, m = map(int, input().split())
g = {}

for line in sys.stdin:
    e -= 1
    a, b, w = map(int, line.split())
    a -= 1
    b -= 1
    if a not in g:
        g[a] = {}
    if b not in g:
        g[b] = {}
    g[a][b] = g[b][a] = w
    if e == 0:
        break
clearings = list(map(lambda x: int(x) - 1, input().split()))

D = [float('inf')] * v
D[0] = 0
pq = [(0, 0)]

while pq:
    dd, vv = heappop(pq)
    if dd == D[vv] and vv in g:
        for nn in g[vv]:
            if D[nn] > dd + g[vv][nn]:
                D[nn] = dd + g[vv][nn]
                heappush(pq, (D[nn], nn))

# Filter non-reachable fruity clearings
clearings = list(filter(lambda x: D[x] != float('inf'), clearings))
if len(clearings) < min(m, k):
    print(-1)
else:
    print(2 * D[sorted(clearings, key=lambda x: D[x])[min(k, m) - 1]])