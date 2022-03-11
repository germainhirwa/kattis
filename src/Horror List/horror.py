import sys
from collections import deque

n, h, l = map(int, input().split())
hh = list(map(int, input().split()))
dd = [float('inf')] * n
vs = [False] * n
g = {}
for line in sys.stdin:
    a, b = map(int, line.split())
    if a not in g:
        g[a] = []
    if b not in g:
        g[b] = []
    g[a].append(b)
    g[b].append(a)

q = deque([(i, 0) for i in hh])
for i in hh:
    vs[i] = True

while q:
    v, d = q.popleft()
    dd[v] = d
    vs[v] = True
    if v in g:
        for w in g[v]:
            if not vs[w]:
                q.append((w, d + 1))
m = max(dd)
for i in range(n):
    if dd[i] == m:
        print(i)
        break