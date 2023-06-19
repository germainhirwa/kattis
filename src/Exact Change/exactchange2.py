for _ in range(int(input())):
    amt = int(input())
    coins = [int(input()) for _ in range(int(input()))]
    dp = [1e9]*(10**5+2)
    dp[0] = 0
    for i in coins:
        for j in range(len(dp)-i-1,-1,-1): dp[j+i] = min(dp[j+i], dp[j]+1)
    for j in range(amt, len(dp)):
        if dp[j] != 1e9: print(j, dp[j]); break