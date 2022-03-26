from heapq import *
import sys

while True:
    v, e, q, s = map(int, input().split())
    if v + e + q + s == 0:
        break

    g = {}
    if e != 0:
        for line in sys.stdin:
            e -= 1
            src, des, d = map(int, line.split())
            if src not in g:
                g[src] = {}
            if des not in g[src]:
                g[src][des] = float('inf')
            g[src][des] = min(g[src][des], d)
            if e == 0:
                break

    D = [float('inf')] * v
    D[s] = 0
    pq = [(0, s)]

    while pq:
        dd, vv = heappop(pq)
        if dd == D[vv] and vv in g:
            for nn in g[vv]:
                if D[nn] > dd + g[vv][nn]:
                    D[nn] = dd + g[vv][nn]
                    heappush(pq, (D[nn], nn))

    if q != 0:
        for line in sys.stdin:
            q -= 1
            k = int(line)
            if D[k] == float('inf'):
                print('Impossible')
            else:
                print(D[k])
            if q == 0:
                break
    print()