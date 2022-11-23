import sys
from heapq import *

def to_i(u, c1, c2):
    return 10**8*u + 10**4*c1 + c2

g = {}
_, m, k1, k2 = map(int, input().split())
for line in sys.stdin:
    if m == 0:
        s, t = map(int, line.split())
        s = to_i(s, 0, 0)
        t = to_i(t, k1, k2)
        break
    m -= 1
    u, v, x, c = map(int, line.split())
    for c1 in range(k1 + 1):
        for c2 in range(k2 + 1):
            nc1, nc2 = c1 + (c == 1), c2 + (c == 2)
            if nc1 > k1 or nc2 > k2: continue
            ou, ov = to_i(u, c1, c2), to_i(v, c1, c2)
            nu, nv = to_i(u, nc1, nc2), to_i(v, nc1, nc2)
            for o, n in [[ou, nv], [ov, nu]]:
                if o not in g:      g[o] = {n: x}
                elif n not in g[o]: g[o][n] = x
                else:               g[o][n] = min(x, g[o][n])

def dijkstra(D, s):
    D[s] = 0
    pq = [(0, s)]
    while pq:
        dd, vv = heappop(pq)
        if dd == D[vv] and vv in g:
            for nn in g[vv]:
                if nn not in D or D[nn] > dd + g[vv][nn]:
                    D[nn] = dd + g[vv][nn]
                    heappush(pq, (D[nn], nn))

D = {}
dijkstra(D, s)
if t not in D:
    print(-1)
else:
    print(D[t])