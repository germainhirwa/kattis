n = int(input())
g = {}
for _ in range(n):
    r = input().split()
    if r[0] not in g:
        g[r[0]] = set()
    for i in range(1, len(r)):
        g[r[0]].add(r[i])
        if r[i] not in g:
            g[r[i]] = set()
        g[r[i]].add(r[0])

from collections import deque
s, d = input().split()
p = {s: None}
vis = {s}
q = deque([s])
while q:
    u = q.popleft()
    if u == d:
        break
    if u in g:
        for v in g[u]:
            if v not in vis:
                vis.add(v)
                q.append(v)
                p[v] = u

path = []
ptr = d
try:
    while ptr:
        path.append(ptr)
        ptr = p[ptr]
    print(*path[::-1])
except:
    print('no route found')