def fill(root, parent, g, dp, k):
    for c in range(k): dp[root][c] = c+1
    for child in g[root]:
        if child == parent: continue
        fill(child, root, g, dp, k)
        for c in range(k): dp[root][c] += min(dp[child][l] for l in range(k) if l != c)

import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**5)
n, k = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u-1].append(v-1), g[v-1].append(u-1)
dp = [[0]*k for _ in range(n)]
try: fill(0, -1, g, dp, k), print(min(dp[0]))
except: print(-1)