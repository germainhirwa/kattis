import sys; input = sys.stdin.readline

class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]
        self.rank = [0]*N
        self.max = [0]*N
        self.size = [1]*N
    def find_set(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find_set(i)) != (y:=self.find_set(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x; self.size[x] += self.size[y]
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]; self.size[y] += self.size[x]

for _ in range(int(input())):
    input(); V = int(input())
    G = []; U = UFDS(V); W = 0
    for _ in range(V-1): a, b, w = map(int, input().split()); G.append((w, a-1, b-1))
    for w, a, b in sorted(G):
        if (x:=U.find_set(a)) != (y:=U.find_set(b)): W += (w+1)*U.size[x]*U.size[y]-1; U.union(a, b)
    print(W)