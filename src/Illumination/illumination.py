import sys; input = sys.stdin.readline
n, r, k = map(int, input().split())
g = [set() for _ in range(2*k)]; gt = [set() for _ in range(2*k)]
rr = [{} for _ in range(n)]; cc = [{} for _ in range(n)]
for i in range(k): a, b = map(int, input().split()); rr[a-1][b-1] = cc[b-1][a-1] = i
for i in range(n):
    for j in rr[i]:
        for dj in range(1, r+1):
            if j+dj >= n: break
            if j+dj in rr[i]: a, b = rr[i][j], rr[i][j+dj]; g[a].add(b+k), g[b].add(a+k), gt[b+k].add(a), gt[a+k].add(b)
    for j in cc[i]:
        for dj in range(1, r+1):
            if j+dj >= n: break
            if j+dj in cc[i]: a, b = cc[i][j], cc[i][j+dj]; gt[a].add(b+k), gt[b].add(a+k), g[b+k].add(a), g[a+k].add(b)
top, vis, scc = [], [0]*2*k, 1
def DFS(s, t):
    stack = [2*s]; a = g if t else gt
    while stack:
        ub = stack.pop()
        u, b = ub//2, ub%2
        if b and t: top.append(u)
        elif not vis[u]:
            vis[u] = scc
            stack.append(2*u+1)
            for v in a[u]:
                if not vis[v]: stack.append(2*v)
    return 1
for i in range(2*k):
    if i not in vis: DFS(i, True)
vis = [0]*2*k
for i in top[::-1]:
    if not vis[i]: scc += DFS(i, False)
for i in range(k):
    if vis[i] == vis[k+i]: print(0), exit(0)
print(1)