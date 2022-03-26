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
            src, des, t0, p, d = map(int, line.split())
            if src not in g:
                g[src] = []
            g[src].append((des, t0, p, d))
            if e == 0:
                break

    D = [float('inf')] * v
    D[s] = 0
    pq = [(0, s)]

    while pq:
        dd, vv = heappop(pq)
        if dd == D[vv] and vv in g:
            for nn, tt, pp, ww in g[vv]:
                # [2, 5, None]
                # dd = 20 -> 22
                if pp != 0:
                    new = (max(dd, tt) - tt % pp + pp - 1) // pp * pp + tt % pp
                else:
                    new = tt
                    if dd > new:
                        continue
                w = new + ww
                if D[nn] > w:
                    D[nn] = w
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