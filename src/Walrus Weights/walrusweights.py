def knapsack(capacity, weights):
    n = len(weights)
    dp = [[float('inf')]*(capacity+1) for _ in range(n+1)]; dp[0][0] = 0
    for i in range(1,n+1):
        dp[i][0] = 0
        for j in range(1,capacity+1):
            if j >= weights[i-1]: dp[i][j] = min(dp[i-1][j-weights[i-1]]+1, dp[i-1][j])
            else: dp[i][j] = dp[i-1][j]
    return dp

import sys; input = sys.stdin.readline
dp = knapsack(2000, [int(input()) for _ in range(int(input()))])[-1]
for d in range(1001):
    for _ in range(2):
        if dp[1000+d] < 10000: print(1000+d), exit(0)
        d = -d