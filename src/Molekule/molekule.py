import sys
from collections import deque

n = int(input())
g = {}
e = []
for line in sys.stdin:
    a, b = map(int, line.split())
    a -= 1
    b -= 1
    if a not in g:
        g[a] = []
    if b not in g:
        g[b] = []
    g[a].append(b)
    g[b].append(a)
    e.append((a, b))

col = [-1] * n
col[0] = 0
q = deque([(0, 0)])
while q:
    u = q.pop()
    if u in g:
        for v in g[u]:
            if col[v] == -1:
                col[v] = 1 - col[u]
                q.append(v)
for a, b in e:
    print(col[a])