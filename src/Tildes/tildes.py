import sys

class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.size = [1 for _ in range(N)]

    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]

    def union(self, i, j):
        x, y = self.find_set(i), self.find_set(j)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
                self.size[x] += self.size[y]
            else:
                self.p[x] = y
                self.size[y] += self.size[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

n, q = map(int, input().split())
ufds = UFDS(n)
for line in sys.stdin:
    c = line.split()
    if len(c) == 2:
        print(ufds.size[ufds.find_set(int(c[-1]) - 1)])
    else:
        ufds.union(int(c[1]) - 1, int(c[2]) - 1)