import sys
from math import hypot

class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.n = N

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            self.n -= 1
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

n, e, p = map(int, input().split())
t, uf, c, el = [], UFDS(n), 0, []
for l in sys.stdin:
    if len(t) != n:
        x, y = map(float, l.split())
        t.append((x, y))
        if len(t) == n:
            for i in range(n):
                for j in range(i+1, n): el.append((i, j, hypot(t[i][0]-t[j][0], t[i][1]-t[j][1])))
    else:
        a, b = map(int, l.split())
        uf.union(a-1, b-1)

for i in range(1, e): uf.union(i-1, i)
for u, v, w in sorted(el, key=lambda x: x[-1]):
    if not uf.is_same_set(u, v):
        uf.union(u, v)
        c += w
    if uf.n == 1: break
print(c)