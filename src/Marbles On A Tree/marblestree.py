import sys
sys.setrecursionlimit(10**5)

while True:
    n = int(input())
    if n == 0:
        break

    g = {}
    dd = [0]
    for _ in range(n):
        line = list(map(int, input().split()))
        dd.append(line[1]-1)
        for k in range(3, len(line)):
            if line[0] not in g: g[line[0]] = []
            g[line[0]].append(line[k])
    vis = [0]*(n+1)
    def dfs(u):
        if vis[u]: return
        vis[u] = 1
        if u in g:
            for v in g[u]:
                dfs(v)
                dd[u] += dd[v]
    for i in range(n): dfs(i+1)
    print(sum(map(abs, dd)))