q, cl = map(int, input().split())
ut = input()
g = {}

for _ in range(q):
    a, b, c = input().split()
    for k in (b, c):
        if k not in g:
            g[k] = []
        g[k].append(a)

# BFS toposort
val = {}
val[ut] = 1
indeg = {}
for u in g:
    for v in g[u]:
        if v not in indeg:
            indeg[v] = 0
        indeg[v] += 1

from collections import deque
q = deque([])
for i in g:
    if i not in indeg:
        q.append(i)

while q:
    u = q.popleft()
    if u in g:
        for v in g[u]:
            indeg[v] -= 1
            if v not in val:
                val[v] = 0
            if u not in val:
                val[u] = 0
            val[v] += val[u] / 2
            if indeg[v] == 0:
                q.append(v)

del val[ut]
best, score = None, 0

for _ in range(cl):
    h = input()
    if h in val and val[h] > score:
        best, score = h, val[h]

print(best)