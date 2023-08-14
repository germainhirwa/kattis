import sys; input = sys.stdin.readline
n, s, t = map(int, input().split())
g = [[*map(int, input().split())] for _ in range(n)]
d = [1e9]*n; d[s] = 0
for _ in range(6): # no need to be n-1
    for i in range(n):
        for j in range(n): d[j] = min(d[j], d[i]+g[i][j])
print(d[t])