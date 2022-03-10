class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.chars = [0 for _ in range(N)]

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
                self.chars[x] = min(self.chars[x], self.chars[y])
            else:
                self.p[x] = y
                self.chars[y] = min(self.chars[x], self.chars[y])
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

import sys

n, m = map(int, input().split())
ufds = UFDS(10001)
words = input().split()
D = {}
for w in words:
    if w not in D:
        D[w] = len(D)
        ufds.chars[D[w]] = len(w)

for line in sys.stdin:
    a, b = line.strip().split()
    for i in [a, b]:
        if i not in D:
            D[i] = len(D)
            ufds.chars[D[i]] = len(i)
    ufds.union(D[a], D[b])

print(sum(map(lambda x: ufds.chars[ufds.find_set(D[x])], words)))