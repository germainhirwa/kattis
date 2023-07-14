import sys; input = sys.stdin.readline
sys.setrecursionlimit(100_000)
n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(1, n): g[int(input())-1].append(i)
ti, to = [0]*n, [0]*n
t, vis = [0], [0]*n

def dfs(v):
    if vis[v]: return
    t[0] += 1; ti[v] = t[0]; vis[v] = 1
    for i in g[v]: dfs(i)
    t[0] += 1; to[v] = t[0]

dfs(0)
for _ in range(q):
    a, b = map(int, input().split()); a -= 1; b -= 1
    print(['Yes', 'No'][ti[b] < ti[a] and to[a] < to[b]])