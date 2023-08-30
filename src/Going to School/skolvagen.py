s = input().strip()
dp = [[1e9, 1e9] for _ in range(len(s)+1)]
dp[0][0] = 0; dp[0][1] = 1
for i in range(1, len(s)+1):
    dp[i][0] = min(dp[i][0], dp[i-1][0]+(s[i-1]!='S'), dp[i-1][1]+1+(s[i-1]!='N'))
    dp[i][1] = min(dp[i][1], dp[i-1][1]+(s[i-1]!='N'), dp[i-1][0]+1+(s[i-1]!='S'))
print(dp[-1][0])