n, s, k = list(map(int, input().split()))
dp = [[0]*(s+5) for _ in range(n+1)]
dp[1][1] = 1
for i in range(1, n):
    for j in range(s+4):
        dp[i+1][j] += dp[i][j]*j/s
        dp[i+1][j+1] += dp[i][j]*(s-j)/s
print(sum(dp[n][k:]))