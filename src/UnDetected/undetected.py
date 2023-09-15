class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N; self.l = [0]*N; self.r = [0]*N
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x; self.l[x] |= self.l[y]; self.r[x] |= self.r[y]
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]; self.l[y] |= self.l[x]; self.r[y] |= self.r[x]
import sys; input = sys.stdin.readline
u = UFDS(n:=int(input()))
p = [[*map(int, input().split())] for _ in range(n)]
for i, (x, y, r) in enumerate(p):
    u.l[i] = int(x < r); u.r[i] = int(x > 200-r); s = u.find(i)
    if u.l[s]*u.r[s]: print(0), exit(0)
for i in range(n):
    x, y, r = p[i]
    for j in range(i):
        x2, y2, r2 = p[j]
        if (x-x2)**2 + (y-y2)**2 < (r+r2)**2: u.union(i, j)
    s = u.find(i)
    if u.l[s]*u.r[s]: print(i); break