import sys
from heapq import *
n, m, s = map(int, input().split())
g = [[] for _ in range(n)]
for l in sys.stdin:
    u, v, t0, p, d = map(int, l.split())
    g[v].append((u, t0, p, d))

D = [-1]*n
D[-1] = s
pq = [(-D[-1], n-1)]
while pq:
    dd, vv = heappop(pq); dd = -dd
    if dd < 0: print('impossible'), exit(0)
    if vv == 0: print(dd), exit(0)
    if dd == D[vv]:
        for nn, tt, pp, ww in g[vv]:
            if dd < ww or tt > dd-ww: continue
            new = tt + (dd-ww-tt)//pp*pp
            if D[nn] < new: D[nn] = new; heappush(pq, (-D[nn], nn))
print('impossible')