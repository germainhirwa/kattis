import sys

x, y = map(int, input().split())
m = []

for line in sys.stdin:
    m.append(list(map(int, line.split())))

class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.sz = [1 for _ in range(N)]
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
                self.sz[x] += self.sz[y]
            else:
                self.p[x] = y
                self.sz[y] += self.sz[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

indeg = {}
ufds = UFDS(x*y)

for i in range(y):
    for j in range(x):
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= i + di < y and 0 <= j + dj < x:
                if m[i][j] == m[i + di][j + dj]:
                    ufds.union(x*i + j, x*(i + di) + (j + dj))

for i in range(y):
    for j in range(x):
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= i + di < y and 0 <= j + dj < x:
                pl, pr = ufds.find_set(x*i + j), ufds.find_set(x*(i + di) + (j + dj))
                if pl not in indeg:
                    indeg[pl] = 0
                if pr not in indeg:
                    indeg[pr] = 0
                if m[i][j] < m[i + di][j + dj]:
                    indeg[pr] += 1
print(sum(map(lambda x: ufds.sz[x], filter(lambda x: indeg[x] == 0, indeg))))