import sys
from heapq import *

g = {}
t = []
n = int(input())
indeg, q = [0]*(n+1), []
for line in sys.stdin:
    ti, _, *p = map(int, line.split())
    t.append(ti)
    v = len(t)
    g[v] = []
    for u in p:
        g[v].append(u)
        indeg[u] += 1
for v in range(n):
    if indeg[v+1] == 0:
        q.append((t[v], v+1))
heapify(q)
top = []
n -= 1
while q:
    tx, u = heappop(q)
    top.append(n-len(top)+tx)
    if u in g:
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0: heappush(q, (t[v-1], v))
print(max(top))