for _ in range(int(input())):
    K, n, m, k = map(int, input().split())
    miss = {m+i*k for i in range(30)}
    dp = [0]*(n+1); dp[0] = 1
    for i in range(1, m): dp[i] = 2**(i-1)
    for i in range(m, n+1):
        for j in range(1, i+1):
            if j not in miss: dp[i] += dp[i-j]
    print(K, dp[n])