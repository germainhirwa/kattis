from collections import deque
import sys

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

for _ in range(int(input())):
    m, cnt = [], 0
    c, r = map(int, input().split())
    for line in sys.stdin:
        cnt += 1
        m.extend(line.strip())
        while len(m) % c != 0:
            m.append(' ')
        if cnt == r:
            break
    D, g = {}, {}
    pos = 0
    for i in range(r):
        for j in range(c):
            if m[pos] in 'AS':
                D[pos] = {}
            if m[pos] != '#':
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= i + dr < r and 0 <= j + dc < c:
                        nxt = pos + c*dr + dc
                        if m[nxt] != '#':
                            if pos not in g:
                                g[pos] = []
                            g[pos].append(nxt)
            pos += 1
    
    el = []
    for ij in D:
        visited = {ij}
        q = deque([(ij, 0)])
        while q:
            rc, d = q.popleft()
            if rc in D and d != 0:
                D[ij][rc] = D[rc][ij] = d
                el.append((ij, rc, d))
            if rc in g:
                for uv in g[rc]:
                    if uv not in visited:
                        visited.add(uv)
                        q.append((uv, d + 1))
    pt2id = {}
    for ij in D:
        pt2id[ij] = len(pt2id)
    ufds = UFDS(len(pt2id))
    el.sort(key=lambda x: x[-1])
    ans = 0
    for src, dst, w in el:
        if ufds.num_sets == 1:
            break
        if not ufds.is_same_set(pt2id[src], pt2id[dst]):
            ufds.union(pt2id[src], pt2id[dst])
            ans += w
    print(ans)