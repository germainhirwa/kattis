n, r, k, x0, a, b = map(int, input().split())

class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]
        self.rank = [0]*N
        self.min = [*range(N)]
    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find_set(i)) != (y:=self.find_set(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x; self.min[x] = min(self.min[y], self.min[x])
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]; self.min[y] = min(self.min[y], self.min[x])

aa = 0
u = UFDS(n)
rr = [0]*n
for _ in range(r):
    x0 = (a*x0+b)%n; rep = u.min[u.find_set(x0)]
    while rr[rep] == k:
        if rep == 0: print('OVERFLOW'), exit(0)
        u.union(rep, rep-1)
        rep = u.min[u.find_set(rep)]
    rr[rep] += 1; aa = (53*aa+rep)%199933
print(aa)