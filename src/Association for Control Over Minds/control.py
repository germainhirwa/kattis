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

n = int(input())
ufds = UFDS(500000)
ans = 0
for line in sys.stdin:
    q = list(map(int, line.split()))
    s, r = q[0], q[1:]
    p = set()
    for i in r:
        p.add(ufds.find_set(i - 1))
    if sum(map(lambda x: ufds.size[x], p)) == s:
        ans += 1
        for i in r[1:]:
            ufds.union(i - 1, r[0] - 1)
print(ans)