import sys, math

n, pos = int(input()), 0
rev, dists = {}, {}
arr = []
for line in sys.stdin:
    x, y, z = map(int, line.split())
    p1 = 1001**2 * x + 1001 * y + z
    for p2 in rev:
        dist = (p1 % 1001 - p2 % 1001)**2 + (p1 // 1001 % 1001 - p2 // 1001 % 1001)**2 + (p1 // 1001**2 % 1001 - p2 // 1001**2 % 1001)**2
        if dist not in dists:
            dists[dist] = [1001**3 * p1 + p2]
            arr.append(dist)
        else:
            dists[dist].append(1001**3 * p1 + p2)
    rev[p1] = pos
    pos += 1
arr = sorted(arr)

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

ufds = UFDS(n)
minmax = 0

# Kruskal's Algorithm
for dist in arr:
    for h in dists[dist]:
        p1, p2 = h // 1001**3, h % 1001**3
        if not ufds.is_same_set(rev[p1], rev[p2]):
            minmax = max(minmax, dist)
            ufds.union(rev[p1], rev[p2])
        if ufds.num_sets == 1:
            # Profit!
            print(math.ceil(minmax**0.5))
            sys.exit(0)