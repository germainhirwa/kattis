dp = [[[0, 0] for _ in range(501)] for _ in range(501)]
for i in range(1, 501):
    for j in range(1, 501):
        for k in range(1, i):
            dp[i][j][1] |= 1-(dp[i-k][j][0]|dp[k][j][0])
            if dp[i][j][1]: break
        for k in range(1, j):
            dp[i][j][0] |= 1-(dp[i][j-k][1]|dp[i][k][1])
            if dp[i][j][0]: break
for _ in range(int(input())): b, d, s = input().split(); b, d = map(int, (b, d)); s, n = int(s[0]=='V'), s.strip(); print(n, f'can{"not"*(1-dp[b][d][s])} win')