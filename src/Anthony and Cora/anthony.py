n, m = map(int, input().split())
p = [0, 0]+[float(input()) for _ in range(n+m-1)][::-1]
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n+1): dp[i][0] = 1
for i in range(1, n+1):
    for j in range(1, m+1): dp[i][j] = p[i+j]*dp[i][j-1] + (1-p[i+j])*dp[i-1][j]
print(dp[-1][-1])