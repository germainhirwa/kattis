q, n, D = map(int, input().split())

# dp[i][d] = number of strings with length i and hamming distance 2n-d
dp = [[0 for _ in range(2*n+1)] for _ in range(n+1)]
f1, f2 = list(map(int, list(input()))), list(map(int, list(input())))
for i in range(q):
    dp[1][(i == f1[0]) + (i == f2[0])] += 1
for i in range(2, n+1):
    for j in range(2*n+1):
        if f1[i-1] == f2[i-1]:
            if j >= 2:
                dp[i][j] += dp[i-1][j-2]
            dp[i][j] += (q-1)*dp[i-1][j]
        else:
            if j >= 1:
                dp[i][j] += 2*dp[i-1][j-1]
            dp[i][j] += (q-2)*dp[i-1][j]
print(dp[n][2*n-D])