import sys
from collections import deque

n = int(input())
g = {}
h = {}
surp, q = {}, deque([])
for line in sys.stdin:
    ti, ki, *sv = map(int, line.split())
    u = len(surp) + 1
    surp[u] = -ti
    for i in range(ki):
        v, w = sv[2*i], sv[2*i+1]
        if v not in g: g[v] = {}
        g[v][u] = w
        surp[u] += w
top = set()
surp[1] = -1
for v in surp:
    if surp[v] < 0:
        q.append(v)
while q:
    u = q.popleft()
    if u in top: continue
    top.add(u)
    if u in g:
        for v in g[u]:
            surp[v] -= g[u][v]
            if surp[v] < 0: q.append(v)
print(n - len(top))