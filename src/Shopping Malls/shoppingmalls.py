import sys
from math import hypot
from collections import deque
from heapq import *

v, e = map(int, input().split())

mall = []
cnt = 0
if v != 0:
    for line in sys.stdin:
        floor, x, y = map(int, line.split())
        mall.append((floor, x, y))
        cnt += 1
        if cnt == v:
            break

g = {}
if e != 0:
    for line in sys.stdin:
        e -= 1
        src, dest, mode = line.strip().split()
        src, dest = int(src), int(dest)
        if src not in g:
            g[src] = {}
        if dest not in g[src]:
            g[src][dest] = float('inf')
        if dest not in g:
            g[dest] = {}
        if src not in g[dest]:
            g[dest][src] = float('inf')

        if mode == 'lift':
            g[src][dest] = min(g[src][dest], 1)
            g[dest][src] = min(g[dest][src], 1)
        elif mode == 'escalator':
            g[src][dest] = min(g[src][dest], 1)
            g[dest][src] = min(g[dest][src], 3*hypot(hypot(mall[src][1] - mall[dest][1], mall[src][2] - mall[dest][2]), 5*(mall[src][0] - mall[dest][0])))
        else:
            w = hypot(hypot(mall[src][1] - mall[dest][1], mall[src][2] - mall[dest][2]), 5*(mall[src][0] - mall[dest][0]))
            g[src][dest] = min(g[src][dest], w)
            g[dest][src] = min(g[dest][src], w)
        if e == 0:
            break

input()
for line in sys.stdin:
    s, t = map(int, line.split())
    D = [float('inf')] * v
    D[s] = 0
    par = [i for i in range(v)]
    pq = [(0, s)]

    while pq:
        dd, vv = heappop(pq)
        if dd == D[vv] and vv in g:
            for nn in g[vv]:
                if D[nn] > dd + g[vv][nn]:
                    par[nn] = vv
                    D[nn] = dd + g[vv][nn]
                    heappush(pq, (D[nn], nn))

    path = deque([])
    curr = t
    while curr != par[curr]:
        path.appendleft(curr)
        curr = par[curr]
    path.appendleft(s)
    print(*path)