from random import choice
N = int(input())
m = [[*map(int, input().split())] for _ in range(N)]

def check(k):
    def aug(l):
        if vis[l]: return 0
        vis[l] = 1
        for r in g[l]:
            if match[r] == -1 or aug(match[r]): match[r] = l; return 1
        return 0
    g = [[] for _ in range(2*N)]
    match, mcbm = [-1]*2*N, 0
    free = set(range(N))
    nfree = len(free)
    for i in range(N):
        for j in range(N):
            if m[i][j] >= k: g[i].append(j+N)
    for l in list(free):
        candidates = [r for r in g[l] if match[r] == -1]
        if candidates:
            mcbm += 1
            free.discard(l)
            match[choice(candidates)] = l
    for f in free:
        vis = [0]*nfree
        mcbm += aug(f)
    return mcbm == N

lo, hi = 1, 10**6
while abs(lo-hi) > 1:
    mid = (lo+hi)//2
    if check(mid): lo = mid
    else: hi = mid-1
for i in range(hi+1, lo-2, -1):
    if check(i): print(i), exit(0)