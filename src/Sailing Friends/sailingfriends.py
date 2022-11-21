class UFDS:
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for _ in range(N)]
        self.boat = [0 for _ in range(N)]
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
                self.boat[x] |= self.boat[y]
            else:
                self.p[x] = y
                self.size[y] += self.size[x]
                self.boat[y] |= self.boat[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

n, b, m = map(int, input().split())
u = UFDS(n)
for i in map(int, input().split()):
    u.boat[i-1] = 1
for _ in range(m):
    a, b = map(int, input().split())
    u.union(a-1, b-1)
s = set()
for i in range(n):
    p = u.find_set(i)
    if not u.boat[p]:
        s.add(p)
print(len(s))