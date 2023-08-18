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
import sys; input = sys.stdin.readline
h = {}; el = []
for i in range(n:=int(input())):
    for j in map(int, input().split()[1:]):
        if j not in h: h[j] = []
        h[j].append(i)
u = UFDS(n)
el = []
for i in h:
    for j in range(len(h[i])-1):
        if u.find_set(h[i][j]) != u.find_set(h[i][j+1]):
            u.union(h[i][j], h[i][j+1]), el.append((h[i][j]+1, h[i][j+1]+1, i))
if len(el) != n-1: print('impossible'), exit(0)
for i in el: print(*i)