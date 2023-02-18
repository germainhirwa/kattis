import sys
from collections import deque

n, k = map(int, input().split())
g, cc = [{} for _ in range(n+1)], 0
for line in sys.stdin:
    a, b, c = map(int, line.split())
    g[a][b] = g[b][a] = c
    cc += c

if k == 1:
    q, vis, D = deque([(1, 0)]), set(), [0]*(n+1)
    while q:
        u, d = q.popleft()
        if u in vis: continue
        vis.add(u)
        D[u] = max(D[u], d)
        for v in g[u]: q.append((v, d+g[u][v]))

    # do it again but different source
    q, vis, D = deque([(max(map(lambda x: x[::-1], enumerate(D)))[1], 0)]), set(), [0]*(n+1)
    while q:
        u, d = q.popleft()
        if u in vis: continue
        vis.add(u)
        D[u] = max(D[u], d)
        for v in g[u]: q.append((v, d+g[u][v]))
    print(max(D)) # longest path from any to any
else:
    print(cc) # every undirected tree has a Eulerian tour