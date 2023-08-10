import sys
d = int(input())
p = [[0, 0], *([*map(int, l.split())] for l in sys.stdin)]
if p[-1][0] != d: p.append([d, 20**9])
dp = [[20**9]*201 for _ in range(d+1)]
dp[0][100] = 0
for i in range(1, len(p)):
    dist = p[i][0]-p[i-1][0]
    for j in range(201-dist):
        for k in range(201-j):
            dp[p[i][0]][j+k] = min(dp[p[i][0]][j+k], dp[p[i-1][0]][j+dist]+k*p[i][1])
ans = min(dp[d][100:])
print('Impossible' if ans == 20**9 else ans)