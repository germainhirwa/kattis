import sys

# n digits, use digits up to k
def tight(n, k):
    # dp[i][j] -> i digits ending in j
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(k+1):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(k+1):
            dp[i][j] = dp[i-1][j]
            if j-1 >= 0:    dp[i][j] += dp[i-1][j-1]
            if j+1 < k+1:   dp[i][j] += dp[i-1][j+1]
    return sum(dp[n])

for line in sys.stdin:
    k, n = map(int, line.split())
    print(100*tight(n, k)/(k+1)**n)