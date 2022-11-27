n, q = int(input()), float(input())
v = []
for _ in range(n): v.append(float(input()))
dp = [[0, 0] for _ in range(n)]
# The trick is to either buy everything or sell everything
dp[0] = [100, (100 - q)/v[0]]
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]*v[i]-q)
    dp[i][1] = max(dp[i-1][1], (dp[i-1][0]-q)/v[i])
print(dp[-1][0])