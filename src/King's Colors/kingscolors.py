MOD = 10**9 + 7
n, k = map(int, input().split())
dp, f = [[0]*(k+1) for _ in range(n+1)], 1
for i in range(1, k+1):
    f = (f*i) % MOD
    dp[i][i] = f
for kk in range(2, k+1):
    for nn in range(1, n+1):
        dp[nn][kk] = (kk*dp[nn-1][kk-1] + (kk-1)*dp[nn-1][kk]) % MOD
print(dp[nn][kk])