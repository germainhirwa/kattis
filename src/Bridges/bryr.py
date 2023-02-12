import sys
from heapq import *

n, m = map(int, input().split())
g = [{} for _ in range(n)]
for line in sys.stdin:
    a, b, c = map(int, line.split())
    a -= 1
    b -= 1
    g[a][b] = g[b][a] = c

def dijkstra(D, s, t):
    D[s] = 0
    pq = [(0, s)]
    while pq:
        dd, vv = heappop(pq)
        if dd == D[vv]:
            for nn in g[vv]:
                if nn not in D or D[nn] > dd + g[vv][nn]:
                    D[nn] = dd + g[vv][nn]
                    heappush(pq, (D[nn], nn))
    return D[t]

print(dijkstra({}, 0, n-1))