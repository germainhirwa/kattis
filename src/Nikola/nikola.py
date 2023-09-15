import sys; input = sys.stdin.readline; sys.setrecursionlimit(2005)
s = [int(input()) for _ in range(int(input()))]
dp = [[1e8]*len(s) for _ in range(len(s))]
for i in range(len(s)): dp[-1][i] = s[-1]
def f(p, j):
    if not (0 <=p<len(s)): return 1e8
    if dp[p][j] != 1e8: return dp[p][j]
    dp[p][j] = s[p]+min(f(p-j, j), f(p+j+1, j+1)); return dp[p][j]
print(f(1, 1))