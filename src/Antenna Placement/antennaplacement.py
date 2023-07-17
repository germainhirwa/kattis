import sys; input = sys.stdin.readline
from random import choice

delta = ((0, 1), (1, 0))
def solve():
    def aug(l):
        if vis[l]: return 0
        vis[l] = 1
        for r in g[l]:
            if match[r] == -1 or aug(match[r]): match[r] = l; return 1
        return 0
    R, C = map(int, input().split())
    m = [input().strip() for _ in range(R)]
    V = R*C
    g = [[] for _ in range(V)]
    u = -1
    for r in range(R):
        for c in range(C):
            u += 1
            if m[r][c] != '*': continue
            for dr, dc in delta:
                if 0<=r+dr<R and 0<=c+dc<C and m[r+dr][c+dc] == '*': g[u].append(u+dr*C+dc), g[u+dr*C+dc].append(u)
    match, mcbm = [-1]*V, 0
    free = set(range(V))
    nfree = len(free)
    for l in list(free):
        candidates = [r for r in g[l] if match[r] == -1]
        if candidates: mcbm += 1; free.discard(l); match[choice(candidates)] = l
    for f in free:
        vis = [0]*nfree
        mcbm += aug(f)
    g2 = [set() for _ in range(V)]
    for i in range(V):
        if match[i] != -1: g2[match[i]].add(i)
    ext, u = 0, -1
    for r in range(R): # add the non-interest places also
        for c in range(C):
            u += 1
            for dr, dc in delta:
                if 0<=r+dr<R and 0<=c+dc<C and (m[r][c] != '*' or m[r+dr][c+dc] != '*'): g[u].append(u+dr*C+dc), g[u+dr*C+dc].append(u)
    for i in range(V):
        r, c = i//C, i%C
        for j in g[i]:
            r2, c2 = j//C, j%C
            if m[r2][c2] == '*' and match[j] == -1: match[j] = i; g2[i].add(j), g2[j].add(i); ext += 1
    print(mcbm//2 + ext)
for _ in range(int(input())): solve()