class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]

import sys; input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split()); u -= 1; v -= 1
    g[u].append(v), g[v].append(u)
cc = 1; vis = [0]*n; uf = UFDS(n); free = []; rep = {}
for i in range(n):
    if vis[i]: continue
    stack = [(i, None)]
    while stack:
        u, par = stack.pop()
        if vis[u]: continue
        if par != None: uf.union(u, par)
        vis[u] = cc; rep[cc] = u
        for v in g[u]:
            if v == par: continue
            if uf.find(u) == uf.find(v): free.append((u, v))
            stack.append((v, u))
    cc += 1
cc -= 2
if len(free) < cc: print('Nej'), exit(0)
print('Ja'), print(cc)
for i in range(cc): print(free[i][0]+1, free[i][1]+1, rep[i+1]+1, rep[i+2]+1)