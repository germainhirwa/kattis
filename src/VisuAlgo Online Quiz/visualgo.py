import sys
from heapq import *
v, e = map(int, input().split())
g = [{} for _ in range(v)]
for l in sys.stdin:
    if e > 0:
        a, b, w = map(int, l.split())
        g[a][b] = w
        e -= 1
    else:
        s, t = map(int, l.split())
        D, pq = {s: (0, 1)}, [(0, s, 1)]
        while pq:
            dd, vv, pp = heappop(pq)
            if dd == D[vv][0] and pp == D[vv][1]:
                for nn in g[vv]:
                    if nn not in D or D[nn][0] > dd + g[vv][nn]:
                        D[nn] = (dd + g[vv][nn], pp)
                        heappush(pq, (D[nn][0], nn, D[nn][1]))
                    elif D[nn][0] == dd + g[vv][nn]:
                        D[nn] = (dd + g[vv][nn], D[nn][1] + pp)
                        heappush(pq, (D[nn][0], nn, D[nn][1]))
        try: print(D[t][1])
        except: print(0)