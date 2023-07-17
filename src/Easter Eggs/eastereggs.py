from random import choice
import sys; input = sys.stdin.readline

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in range(B, B+R):
        if abs(pts[l]-pts[r]) > K: continue
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

N, B, R = map(int, input().split())
pts = [complex(*map(int, input().split())) for _ in range(B+R)]
V = B+R
lo, hi = 0, 1e6
while abs(lo-hi) > 1e-9:
    K = (lo+hi)/2
    match, mcbm = [-1]*V, 0
    free = set(range(B))
    nfree = len(free)
    for l in list(free):
        candidates = [r for r in range(B, B+R) if abs(pts[l]-pts[r]) <= K and match[r] == -1]
        if candidates:
            mcbm += 1
            free.discard(l)
            match[choice(candidates)] = l
    for f in free:
        vis = [0]*nfree
        mcbm += aug(f)
    if V-mcbm >= N: lo = K
    else: hi = K
print(K)