import sys
from collections import deque

input()
grid = []
for line in sys.stdin:
    grid.append(list(map(int, [0] + list(line.strip()) + [0])))
grid.insert(0, [0]*len(grid[0]))
grid.append([0]*len(grid[0]))

class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.per = [0 for _ in range(N)]

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

n, m  = len(grid), len(grid[0])
u = UFDS(n*m)
q = deque([0])
vis = set()
while q:
    v = q.popleft()
    if v in vis:
        continue
    vis.add(v)
    r, c = v//m, v%m
    if grid[r][c] == 0:
        check = 0
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if 0 <= r + dr < n and 0 <= c + dc < m:
                if not grid[r + dr][c + dc]:
                    check += (dr + dc) == -1
                    u.union(r*m+c, (r+dr)*m+(c+dc))
                    q.append((r+dr)*m+(c+dc))
        p = u.find_set(r*m+c)
        u.per[p] += 4 - 2*check
print(u.per[u.find_set(0)] - 2*(n+m))