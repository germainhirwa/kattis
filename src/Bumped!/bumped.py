import sys
from heapq import *

n, m, _, s, t = map(int, input().split())
g = {}

for line in sys.stdin:
    if m != 0:
        i, j, c = map(int, line.split())
        if i not in g:
            g[i] = {}
            g[i + n] = {}
        if j not in g:
            g[j] = {}
            g[j + n] = {}
        g[i][j] = g[j][i] = g[i + n][j + n] = g[j + n][i + n] = c
        m -= 1
    else:
        u, v = map(int, line.split())
        if u not in g:
            g[u] = {}
        g[u][v + n] = 0

D = [float('inf')] * (2 * n)
D[s] = 0
pq = [(0, s)]

while pq:
    dd, vv = heappop(pq)
    if dd == D[vv] and vv in g:
        for nn in g[vv]:
            if D[nn] > dd + g[vv][nn]:
                D[nn] = dd + g[vv][nn]
                heappush(pq, (D[nn], nn))
print(min(D[t], D[t + n]))