LIMIT = 10**4
spf = list(range(LIMIT+1))
primes = set()
p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.add(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
grid = [[0]*100 for _ in range(100)]
def fill():
    r, c, e = 50, 49, 1
    dr, dc = 0, 1
    for s in range(100):
        for _ in range(2):
            for _ in range(s+1):
                grid[r][c] = e
                if r == c == 0: return
                r += dr; c += dc; e += 1
            dr, dc = -dc, dr
fill()
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
g = [[] for _ in range(10**4)]
for r in range(100):
    for c in range(100):
        if grid[r][c] not in primes:
            for dr, dc in delta:
                if 0<=r+dr<100 and 0<=c+dc<100 and grid[r+dr][c+dc] not in primes: g[grid[r][c]-1].append(grid[r+dr][c+dc]-1)

import sys
from collections import deque
c = 1
for l in sys.stdin:
    a, b = map(lambda x: int(x)-1, l.split())
    q, v, f = deque([(a, 0)]), {a}, 0
    while q:
        u, d = q.popleft()
        if u == b: f = 1; break
        for i in g[u]:
            if i not in v: v.add(i), q.append((i, d+1))
    print(f'Case {c}: {d if f else "impossible"}'); c += 1