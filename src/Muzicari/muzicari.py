t, n = map(int, input().split())
w = [*map(int, input().split())]
dp = [[float('inf')]*(t+1) for _ in range(n+1)]; dp[0][0] = 0
for i in range(1,n+1):
    for j in range(1,t+1):
        if j >= w[i-1]: dp[i][j] = min(dp[i-1][j-w[i-1]]+1, dp[i-1][j])
        else: dp[i][j] = dp[i-1][j]
k = []; s = n; tt = t
while dp[s][tt] == float('inf'): tt -= 1
while tt:
    if dp[s-1][tt-w[s-1]] == dp[s][tt]-1: tt -= w[s-1]; s -= 1; k.append(s)
    else: s -= 1
ans = [0]*n; prev = k[0]
for i in k[1:]: ans[i] = ans[prev]+w[prev]; prev = i
l = [*({*range(n)}-{*k})]; prev = l[0]
for i in l[1:]: ans[i] = ans[prev]+w[prev]; prev = i
print(*ans)