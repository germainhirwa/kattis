from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

N, M = map(int, input().split())
g = [[] for _ in range(N+M)]
match, mcbm = [-1]*(N+M), 0
free = set(range(N))
nfree = len(free)
for r in range(N):
    _, *a = map(int, input().split())
    for l in a: g[r].append(l+N-1)
for l in list(free):
    candidates = [r for r in g[l] if match[r] == -1]
    if candidates:
        mcbm += 1
        free.discard(l)
        match[choice(candidates)] = l
for f in free:
    vis = [0] * nfree
    mcbm += aug(f)
print(mcbm)