import sys; input = sys.stdin.readline
n = int(input()); s = input().strip()
dp = [[float('inf')]*3 for _ in range(n)]; dp[0] = [0]*3
for i in range(1, n):
    if s[i] == '.':
        dp[i][0] = dp[i-1][0]+1
        dp[i][1] = dp[i-1][1]+2
        dp[i][2] = dp[i-1][2]+2
    elif s[i] == 'S':
        dp[i][0] = dp[i-1][1]+2
        dp[i][1] = dp[i-1][2]+2
    else:
        dp[i][0] = dp[i-1][0]+1
        dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1]+2)
        dp[i][2] = min(dp[i-1][1], dp[i-1][2])+2
k = min(dp[-1])
print(k if k < 1e9 else -1)