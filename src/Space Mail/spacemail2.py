# A much faster alternative, under 2 seconds
import sys, math

n, pos = int(input()), 0
rev, dists = {}, {}
for line in sys.stdin: # base 1001
    x, y, z = map(int, line.split())
    p1 = 1002001 * x + 1001 * y + z
    for p2 in rev:
        dist = math.ceil(math.sqrt(
            (z - p2 % 1001)**2 +
            (y - p2 // 1001 % 1001)**2 +
            (x - p2 // 1002001 % 1001)**2
        ))
        if dist not in dists:
            dists[dist] = []
        dists[dist].append(1003003001 * p1 + p2)
    rev[p1] = pos
    pos += 1

# UFDS
class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.num_sets = N

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            self.num_sets -= 1
            x, y = self.find_set(i), self.find_set(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

ufds, minmax = UFDS(n), 0

# Kruskal's Algorithm, slightly modified
dist = 0
while True:
    if dist in dists:
        for h in dists[dist]:
            p1, p2 = h // 1003003001, h % 1003003001
            if not ufds.is_same_set(rev[p1], rev[p2]):
                minmax = max(minmax, dist)
                ufds.union(rev[p1], rev[p2])
            if ufds.num_sets == 1:
                # Profit!
                print(minmax)
                sys.exit(0)
    dist += 1