from heapq import *
from array import *
n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]
dp = [array('i', [10**8]*(k+1)) for _ in range(n+1)]; dp[0][0] = 0
cost = [array('i', [0]*(n+1)) for _ in range(n+1)]
for i in range(n):
    l, r = [], []; sl = sr = 0
    for j in range(i, n):
        if l and w[j] >= -l[0]: heappush(r, w[j]); sr += w[j]
        else: heappush(l, -w[j]); sl += w[j]
        while abs(len(l) - len(r)) > 1:
            if len(l) < len(r): sl += r[0]; sr -= r[0]; heappush(l, -heappop(r))
            else: sr -= l[0]; sl += l[0]; heappush(r, -heappop(l))
        if len(l) > len(r): cost[i][j+1] = sr-sl-l[0]*(len(l)-len(r))
        else: cost[i][j+1] = sr-sl+r[0]*(len(l)-len(r))
for i in range(1, k+1):
    for j in range(1, n+1):
        dp[j][i] = min(dp[l][i-1]+cost[l][j] for l in range(j))
print(dp[n][k])