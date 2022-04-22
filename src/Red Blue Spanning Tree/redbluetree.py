import sys
n, m, k = map(int, input().split())
g, r, b = [], [], []

# UFDS
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

for line in sys.stdin:
    c, f, t = line.split()
    f, t = map(int, [f, t])
    f -= 1
    t -= 1
    if c == 'R':
        d = r
    else:
        d = b
    d.append((f, t))
    g.append((f, t))

use = set()
ufds = UFDS(n)

for edge in r:
    u, v = edge
    if not ufds.is_same_set(u, v):
        ufds.union(u, v)

for edge in b:
    u, v = edge
    if not ufds.is_same_set(u, v):
        use.add(edge) # need to link the red forests

ufds = UFDS(n) # reset UFDS
st = []
cb = 0

for edge in use:
    if cb == k:
        break
    u, v = edge
    if not ufds.is_same_set(u, v):
        st.append(edge)
        ufds.union(u, v)
        cb += 1

for edge in b:
    if cb == k:
        break
    u, v = edge
    if not ufds.is_same_set(u, v):
        st.append(edge)
        ufds.union(u, v)
        cb += 1

if cb != k:
    print(0)
else:
    for edge in r:
        u, v = edge
        if not ufds.is_same_set(u, v):
            ufds.union(u, v)
            st.append(edge)
    print(int(len(st) == n - 1))