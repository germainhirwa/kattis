from collections import *
from heapq import *
n, *c, v = map(int, input().split())
s = (c[0], *(0 for _ in range(n-1)))
INF = float('inf'); D = defaultdict(lambda: INF); D[s] = 0; pq = [(0, s)]
while pq:
    dd, vv = heappop(pq)
    if vv[0] == v: print(dd), exit(0)
    if dd != D[vv]: continue
    for i in range(n):
        for j in range(n):
            if i == j or not vv[i] or vv[j] == c[j]: continue
            fill = min(vv[i], c[j]-vv[j])
            nn = [*vv]; nn[i] -= fill; nn[j] += fill; nn = tuple(nn)
            if D[nn] > (new:=dd+fill): D[nn] = new; heappush(pq, (new, nn))
print('impossible')