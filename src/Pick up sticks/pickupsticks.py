from collections import deque

v, e = map(int, input().split())
g = {}
indeg = [0]*v
for _ in range(e):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    if i not in g: g[i] = []
    g[i].append(j)
    indeg[j] += 1
q = deque()
for i in range(v):
    if not indeg[i]: q.append(i)
topo = []
while q:
    u = q.popleft()
    topo.append(u)
    if u in g:
        for u2 in g[u]:
            indeg[u2] -= 1
            if not indeg[u2]: q.append(u2)
if len(topo) == v:
    for i in topo: print(i+1)
else:
    print('IMPOSSIBLE')