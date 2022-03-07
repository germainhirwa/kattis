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

v, e = map(int, input().split())
ufds = UFDS(v)
cc, w = {}, []
for _ in range(v):
    w.append(int(input()))
for _ in range(e):
    ufds.union(*list(map(int, input().split())))
for i in range(v):
    p = ufds.find_set(i)
    if p not in cc:
        cc[p] = 0
    cc[p] += w[i]
print(['IMPOSSIBLE', 'POSSIBLE'][int(set(cc.values()) == {0})])