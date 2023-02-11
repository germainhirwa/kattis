from heapq import *

while True:
    n = int(input())
    if n == 0: break
    g, rev = {}, {}
    indeg = [0]*n
    for _ in range(n):
        pkg, *deps = input().split()
        if pkg not in rev: rev[pkg] = len(rev)
        for dep in deps:
            if dep not in rev: rev[dep] = len(rev)
            if rev[dep] not in g: g[rev[dep]] = []
            g[rev[dep]].append(rev[pkg])
        indeg[rev[pkg]] = len(deps)
    pkgs = dict(map(reversed, rev.items()))
    q = []
    cmp = lambda x: pkgs[x]
    for i in range(len(rev)):
        if not indeg[i]: heappush(q, (cmp(i), i))
    topo = []
    while q:
        _, u = heappop(q)
        topo.append(u)
        if u in g:
            for u2 in g[u]:
                indeg[u2] -= 1
                if not indeg[u2]: heappush(q, (cmp(u2), u2))
    res = list(map(cmp, topo))
    if len(res) != n:
        print('cannot be ordered')
    else:
        for pkg in res: print(pkg)
    print()