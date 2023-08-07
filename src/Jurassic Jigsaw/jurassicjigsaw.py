class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]
        self.rank = [0]*N
    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find_set(i)) != (y:=self.find_set(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]

n, k = map(int, input().split())
dnas = [input() for _ in range(n)]
u = UFDS(n)
el = []
for i in range(n-1):
    for j in range(i+1, n):
        d = 0
        for kk in range(k): d += dnas[i][kk] != dnas[j][kk]
        el.append((d, i, j))
cost, t = 0, []; el.sort()
for w, a, b in el:
    if u.find_set(a) != u.find_set(b): cost += w; t.append((a, b)); u.union(a, b)
print(cost)
for a, b in t: print(a, b)