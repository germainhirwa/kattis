n = int(input())
MOD = 10**9 + 7
a, b = [0] + list(map(int, input().split())), [0, 0] + list(map(int, input().split())) + [0]
dp = [[0, 0] for _ in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1): dp[i] = [(dp[i-1][0]*(a[i]+b[i]) + dp[i-1][1]*(a[i]+b[i]-1)) % MOD, (dp[i-1][0]*b[i+1] + dp[i-1][1]*b[i+1]) % MOD]
print(dp[i][0])