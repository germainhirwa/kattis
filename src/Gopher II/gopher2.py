from random import choice
from math import hypot

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

while True:
    try:
        n, m, s, v = map(int, input().split())
        td = s*v
        g, g1, g2 = [[] for _ in range(n+m)], [], []
        match, mcbm = [-1]*(n+m), 0
        free = set(range(n))
        nfree = len(free)
        for _ in range(n):
            a, b = map(float, input().split())
            g1.append((a, b))
        for _ in range(m):
            a, b = map(float, input().split())
            g2.append((a, b))
        for i, (a, b) in enumerate(g1):
            for j, (c, d) in enumerate(g2):
                if hypot(a-c, b-d) <= td: g[i].append(j+n)
        for l in list(free):
            candidates = [r for r in g[l] if match[r] == -1]
            if candidates:
                mcbm += 1
                free.discard(l)
                match[choice(candidates)] = l
        for f in free:
            vis = [0] * nfree
            mcbm += aug(f)
        print(n-mcbm)
    except: break