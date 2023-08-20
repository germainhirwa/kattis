import sys; input = sys.stdin.readline
v = []; n = int(input()); cc = ff = rr = 0
for _ in range(n):
    d, c, f, u = map(int, input().split())
    if c+u <= f: ff += d # obvious L
    elif f+u < c: cc += d # obvious W
    else: v.append((d, max((c+f+u+2)//2-c, 0))); rr += d
win = (cc+ff+rr+2)//2-cc
if rr < win: print('impossible'), exit(0)
cap = rr-win; m = len(v)
dp = [[0]*(cap+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,cap+1):
        if j >= v[i-1][0]: dp[i][j] = max(dp[i-1][j-v[i-1][0]]+v[i-1][1], dp[i-1][j])
        else: dp[i][j] = dp[i-1][j]
print(sum(i[1] for i in v)-dp[-1][-1])