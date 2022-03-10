class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.size = [1 for _ in range(N)]

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
                self.size[x] += self.size[y]
            else:
                self.p[x] = y
                self.size[y] += self.size[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

import sys

for line in sys.stdin:
    n, r, a, b, c = map(int, line.split())
    ufds = UFDS(n)
    for _ in range(n):
        r = (r * a + b) % c
        x = r % n
        r = (r * a + b) % c
        y = r % n
        if x == y:
            r = (r * a + b) % c
            x = r % n
            r = (r * a + b) % c
            y = r % n
        ufds.union(x, y)
    s = {}
    nd = 0
    for i in range(n):
        if ufds.p[i] == i:
            nd += 1
            size = ufds.size[i]
            if size not in s:
                s[size] = 0
            s[size] += 1

    print(nd, end=' ')
    for k in sorted(s, reverse=True):
        if s[k] == 1:
            print(k, end=' ')
        else:
            print(f'{k}x{s[k]}', end=' ')
    print()