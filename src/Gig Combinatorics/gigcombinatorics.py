import sys; input = sys.stdin.readline
n = int(input()); a = [*map(int,input().split())]
o = r = 0; dp = [0]*(n+1); m = 10**9+7
for i in range(n):
    if a[i] == 1: o += 1; dp[i+1] = dp[i]
    elif a[i] == 2: dp[i+1] = (2*dp[i]+o)%m
    else: dp[i+1] = dp[i]; r += dp[i]; r %= m
print(r)