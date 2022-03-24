import sys
v, e, h, l = map(int, input().split())

if h == l:
    print('leave')
    sys.exit(0)

deg = [0] * v
g = []
for _ in range(v):
    g.append([])

for line in sys.stdin:
    a, b = map(int, line.split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    deg[a] += 1
    deg[b] += 1

p = deg.copy()

from collections import deque
q = deque([l - 1])
p[l - 1] = 0

while q:
    c = q.popleft()
    for n in g[c]:
        if p[n] != 0:
            p[n] -= 1
            if p[n] <= deg[n] // 2:
                q.append(n)
                p[n] = 0
print(['leave', 'stay'][int(bool(p[h - 1]))])