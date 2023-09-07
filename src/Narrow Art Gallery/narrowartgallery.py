n, k = map(int, input().split())
c = [[0, 0]] + [[*map(int, input().split())] for _ in range(n)]
dp = [[[-float('inf')]*(k+1) for _ in range(3)] for _ in range(n+1)]
for i in range(3): dp[0][i][0] = 0
for idx in range(1, n+1):
    for state in range(3):
        for kk in range(k+1):
            if state == 0: dp[idx][state][kk] = c[idx][0]+c[idx][1]+max(dp[idx-1][i][kk] for i in range(3))
            elif state == 1 and kk: dp[idx][state][kk] = c[idx][0]+max(dp[idx-1][i][kk-1] for i in range(3) if i != 2)
            elif state == 2 and kk: dp[idx][state][kk] = c[idx][1]+max(dp[idx-1][i][kk-1] for i in range(3) if i != 1)
print(max(r[-1] for r in dp[-1]))