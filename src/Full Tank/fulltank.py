from heapq import *
import sys

MAX_C = 101

n, m = map(int, input().split())
p = list(map(int, input().split()))
g = {}
for line in sys.stdin:
    m -= 1
    u, v, d = map(int, line.split())
    for _ in range(2):
        if u not in g:
            g[u] = {v: d}
        elif v not in g[u]:
            g[u][v] = d
        else:
            g[u][v] = min(g[u][v], d)
        u, v = v, u
    if m == 0:
        break

def dijkstra(D, s, e, c):
    D[MAX_C*s] = 0
    pq = [(0, MAX_C*s)]
    while pq:
        dd, vvff = heappop(pq)
        vv, ff = vvff // MAX_C, vvff % MAX_C
        vf = MAX_C*vv + ff
        if dd == D[vf] and vv in g:
            if ff < c and (vf + 1 not in D or D[vf + 1] > dd + p[vv]):
                D[vf + 1] = dd + p[vv]
                heappush(pq, (D[vf + 1], vf + 1))
            for nn in g[vv]:
                nf = MAX_C*nn + ff - g[vv][nn]
                if ff >= g[vv][nn] and (nf not in D or D[nf] > dd):
                    D[nf] = dd
                    if nn == e: return
                    heappush(pq, (D[nf], nf))

input()
for line in sys.stdin:
    c, s, e = map(int, line.split())
    D = {}
    dijkstra(D, s, e, c)
    res = float('inf')
    for i in range(c + 1):
        if MAX_C*e + i in D:
            res = min(res, D[MAX_C*e + i])
    if res == float('inf'):
        print('impossible')
    else:
        print(res)