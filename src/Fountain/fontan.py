import sys
from collections import deque

m, q = [], deque([])
r, c = map(int, input().split())
for line in sys.stdin:
    m.append(list(line.strip()))
for i in range(r):
    for j in range(c):
        if m[i][j] == 'V':
            q.append(c*i+j)

vis = set()
while q:
    u = q.popleft()
    ru, cu = u // c, u % c
    if u < (r-1)*c:
        if m[ru + 1][cu] != '#':
            if (ru + 1)*c + cu not in vis:
                m[ru + 1][cu] = 'V'
                vis.add((ru + 1)*c + cu)
                q.append((ru + 1)*c + cu)
        else:
            if cu > 0 and m[ru][cu - 1] != '#':
                if u - 1 not in vis:
                    m[ru][cu - 1] = 'V'
                    vis.add(u - 1)
                    q.append(u - 1)
            if cu < c - 1 and m[ru][cu + 1] != '#':
                if u + 1 not in vis:
                    m[ru][cu + 1] = 'V'
                    vis.add(u + 1)
                    q.append(u + 1)

for row in m:
    print(''.join(row))