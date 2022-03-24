from heapq import *
from collections import deque
import sys

v, e = map(int, input().split())
g = {}

for line in sys.stdin:
    a, b, w = map(int, line.split())
    if a not in g:
        g[a] = {}
    if b not in g:
        g[b] = {}
    g[a][b] = g[b][a] = w

D = [float('inf')] * v
D[1] = 0
pq = [(0, 1)]

rem = [i for i in range(v)]
while pq:
    dd, vv = heappop(pq)
    if dd == D[vv] and vv in g:
        for nn in g[vv]:
            if D[nn] > dd + g[vv][nn]:
                D[nn] = dd + g[vv][nn]
                rem[nn] = vv
                heappush(pq, (D[nn], nn))

for i in range(v):
    if rem[i] != i:
        del g[rem[i]][i]

par = [i for i in range(v)]
q = deque([1])
vis = {1}

while q:
    u = q.popleft()
    if u in g:
        for n in g[u]:
            if n not in vis:
                par[n] = u
                vis.add(n)
                q.append(n)

path = []
ptr = 0
while par[ptr] != ptr:
    path.append(ptr)
    ptr = par[ptr]
if ptr != 1:
    print('impossible')
else:
    path.append(1)
    print(len(path), *path)