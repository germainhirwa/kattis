import sys
from heapq import *

n, k = map(int, input().split())
g = {}
pos, it = [0]*(n**2), 0
hs = {0: [n**2]}
for line in sys.stdin:
    for i, e in enumerate(map(int, line.split())):
        pos[it*n+i] = e
        if e not in hs: hs[e] = []
        hs[e].append(it*n+i)
    it += 1

s = n**2
g = {s: {}}
try:
    for i in range(k):
        for n1 in hs[i]:
            for n2 in hs[i+1]:
                r1, c1, r2, c2 = n1//n, n1%n, n2//n, n2%n
                if n1 not in g: g[n1] = {}
                g[n1][n2] = abs(r1-r2) + abs(c1-c2)
    for i in hs[1]: g[s][i] = 0
    D = {s: 0}
    pq = [(0, s)]
    while pq:
        dd, vv = heappop(pq)
        if dd == D[vv] and vv in g:
            for nn in g[vv]:
                if nn not in D or D[nn] > dd + g[vv][nn]:
                    D[nn] = dd + g[vv][nn]
                    heappush(pq, (D[nn], nn))
    print(min(map(lambda x: D[x], hs[max(hs)])))
except: print(-1)