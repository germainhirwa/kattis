import sys
from collections import deque

r, c = map(int, input().split())
m = []
g = {}

for line in sys.stdin:
    m.append(list(map(int, list(line.strip()))))

for i in range(r):
    for j in range(c):
        d = m[i][j]
        if d == 0:
            continue
        for dr in [0, d, -d]:
            for dc in [0, d, -d]:
                if dr + dc != 0 and dr * dc == 0:
                    if 0 <= i + dr < r and 0 <= j + dc < c:
                        if c*i + j not in g:
                            g[c*i + j] = []
                        g[c*i + j].append(c*(i + dr) + j + dc)

q = deque([(0, 0)])
vis = {0}
while q:
    u, d = q.popleft()
    if u in g:
        for v in g[u]:
            if v == r*c - 1:
                print(d + 1)
                sys.exit(0)
            if v not in vis:
                vis.add(v)
                q.append((v, d + 1))
print(-1)