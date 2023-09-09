import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
src = input().strip(); dst = input().strip()
g = [[] for _ in range(m+2)]; r = {src: 0, dst: 1}; q = [src, dst]
for _ in range(m): q.append(input().strip()); r[q[-1]] = len(r)
v = {*q}
for i in range(m+2):
    s = q[i]; t = [*s]; d = 1
    for j in range(n):
        for _ in range(2):
            o = t[j]
            t[j] = str((int(s[j])+d)%10)
            if (c:=''.join(t)) in v: g[i].append(r[c])
            t[j] = o; d = -d
p = [None]*(m+2); vis = [0]*(m+2)
dq = deque([(r[src], None)])
while dq:
    u, par = dq.popleft()
    if vis[u]: continue
    vis[u] = 1; p[u] = par
    if q[u] == dst:
        path = []; ptr = u
        while ptr != None: path.append(ptr); ptr = p[ptr]
        print(len(path)-1)
        for i in path[::-1]: print(q[i])
        exit(0)
    for vv in g[u]: dq.append((vv, u))
print('Neibb')