import sys; input = sys.stdin.readline
n, m = map(int, input().split())
g = [{} for _ in range(n)]
for _ in range(m):
    a, b, x, y, z = map(int, input().split())
    g[a-1][b-1] = (x, y, z); g[b-1][a-1] = (-x, -y, -z)
stack = []; vis = [0]*n; D = [None]*n
for i in range(n):
    if vis[i]: continue
    stack.append((i, 0, 0, 0))
    while stack:
        u, x, y, z = stack.pop()
        if vis[u] and D[u] != (x, y, z): print('Neibb'), exit(0)
        elif vis[u]: continue
        vis[u] = 1; D[u] = (x, y, z)
        for v in g[u]:
            dx, dy, dz = g[u][v]
            stack.append((v, x+dx, y+dy, z+dz))
print('Jebb')