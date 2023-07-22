import sys; input = sys.stdin.readline
n, m, s, t = map(int, input().split())
q = [[0]*n for _ in range(t+1)]
g = [[] for _ in range(n)]
for _ in range(m): a, b = map(int, input().split()); g[a].append(b), g[b].append(a)
q[0][s] = 1
for i in range(t):
    for u in range(n):
        if q[i][u]:
            for v in g[u]: q[i+1][v] += q[i][u]
print(sum(q[t]))