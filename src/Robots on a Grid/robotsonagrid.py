import sys
from collections import deque

MOD, n, m = 2**31-1, int(input()), []
for line in sys.stdin: m.append(list(map(lambda x: x == '.', line.strip())))
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    if m[i][0]: dp[i][0] = 1
    else: break
for i in range(n):
    if m[0][i]: dp[0][i] = 1
    else: break
for i in range(1, n):
    for j in range(1, n):
        if m[i][j]: dp[i][j] = (dp[i-1][j]%MOD + dp[i][j-1]%MOD)%MOD

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
if dp[-1][-1]: print(dp[-1][-1])
else:
    q, vis = deque([(0, 0)]), {(0, 0)}
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            new_r, new_c = r+dr, c+dc
            if 0 <= new_r < n and 0 <= new_c < n and m[new_r][new_c] and (new_r, new_c) not in vis:
                if new_r == new_c == n-1:
                    print('THE GAME IS A LIE')
                    sys.exit(0)
                q.append((new_r, new_c))
                vis.add((new_r, new_c))
    print('INCONCEIVABLE')