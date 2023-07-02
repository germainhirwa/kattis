from random import choice

def md(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in range(V, 2*V):
        if md(pts[r], pts[l]) <= K and (match[r] == -1 or aug(match[r])): match[r] = l; return 1
    return 0

V = int(input())
pts = [list(map(int, input().split())) for _ in range(2*V)]
lo, hi = 0, 10**9
while hi > lo:
    K = (lo + hi)//2
    match, mcbm = [-1]*2*V, 0
    free = set(range(V))
    for l in list(free):
        candidates = [r for r in range(V, 2*V) if md(pts[r], pts[l]) <= K and match[r] == -1]
        if candidates:
            mcbm += 1
            free.discard(l)
            match[choice(candidates)] = l
    for f in free:
        vis = [0]*V
        mcbm += aug(f)
    if mcbm == V: hi = K
    else: lo = K + 1
print(lo)