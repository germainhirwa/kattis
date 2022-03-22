import sys
from collections import deque

t, r, c = map(int, input().split())
m = []
g = {}

for line in sys.stdin:
    m.append(list(line.strip()))

for i in range(r):
    for j in range(c):
        d = m[i][j]
        pos = c*i + j
        if d == 'S':
            s = pos
        for dr in [0, -1, 1]:
            for dc in [0, -1, 1]:
                if dr + dc != 0 and dr * dc == 0:
                    if 0 <= i + dr < r and 0 <= j + dc < c:
                        if d != '1':
                            dest = c*(i + dr) + j + dc
                            if pos not in g:
                                g[pos] = []
                            if (dr, dc) == (-1, 0) and m[i + dr][j + dc] in ['0', 'D', 'S']:
                                g[pos].append(dest)
                            if (dr, dc) == (0, -1) and m[i + dr][j + dc] in ['0', 'R', 'S']:
                                g[pos].append(dest)
                            if (dr, dc) == (1, 0) and m[i + dr][j + dc] in ['0', 'U', 'S']:
                                g[pos].append(dest)
                            if (dr, dc) == (0, 1) and m[i + dr][j + dc] in ['0', 'L', 'S']:
                                g[pos].append(dest)

q = deque([(s, 0)])
vis = {s}
while q:
    u, d = q.popleft()
    if u // c in [0, r - 1] or u % c in [0, c - 1]:
        if d <= t:
            print(d)
            sys.exit(0)
    if u in g:
        for v in g[u]:
            if v not in vis:
                vis.add(v)
                q.append((v, d + 1))
print('NOT POSSIBLE')