import sys
from heapq import *

def dijkstra(g, s, t, ops):
    D, pq = {s: 0}, [(0, s)]
    while pq:
        dd, vv = heappop(pq)
        if vv == t: break
        if dd == D[vv]:
            if vv not in g:
                g[vv] = {}
                for op, c in ops:
                    nn = vv
                    for i, o in enumerate(op):
                        if o in 'SC': nn |= 1 << l-1-i
                        if o in 'FC': nn ^= 1 << l-1-i
                    if nn != vv:
                        if nn not in g[vv]: g[vv][nn] = c
                        else: g[vv][nn] = min(g[vv][nn], c)
            for nn in g[vv]:
                val = dd + g[vv][nn]
                if nn not in D or D[nn] > val:
                    D[nn] = val
                    heappush(pq, (val, nn))
    if t not in D: return 'NP'
    return D[t]

input()
l, nop, nw = 0, 0, 0
for line in sys.stdin:
    if nw == 0:
        l, nop, nw = map(int, line.split())
        ops = []
    elif nop != 0:
        qop, c = line.split()
        ops.append((qop, int(c)))
        nop -= 1
        if nop == 0: res, g = [], {}
    elif nw != 0:
        b1, b2 = line.split()
        res.append(dijkstra(g, int(b1, 2), int(b2, 2), ops))
        nw -= 1
        if nw == 0: print(*res)