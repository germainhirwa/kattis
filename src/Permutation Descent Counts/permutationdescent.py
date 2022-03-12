import sys
input()

SIZE = 101
dp = []
for _ in range(SIZE):
    dp.append([0] * SIZE)
dp[0][0] = 1
for i in range(SIZE - 1):
    for j in range(i + 1):
        dp[i + 1][j] += dp[i][j] * (j + 1)
        dp[i + 1][j + 1] += dp[i][j] * (i + 1 - j)

for line in sys.stdin:
    c, n, k = map(int, line.split())
    print(c, dp[n-1][k] % 1001113)