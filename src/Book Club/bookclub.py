from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

V, E = map(int, input().split())
g = [[] for _ in range(V)]
match, mcbm = [-1]*(V), 0
free = set(range(V))
nfree = len(free)
for _ in range(E):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
for l in list(free):
    candidates = [r for r in g[l] if match[r] == -1]
    if candidates:
        mcbm += 1
        free.discard(l)
        match[choice(candidates)] = l
for f in free:
    vis = [0] * nfree
    mcbm += aug(f)
print(['NO', 'YES'][mcbm == V])