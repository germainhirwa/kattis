v, e = map(int, input().split())
g = [{} for _ in range(v)]
for _ in range(e):
    a, b, w = map(int, input().split())
    g[a][b] = w
def dfs(s):
    vis.add(s)
    for t in g[s]:
        if t in vis: return t, s
        p[t] = s
        if (u:=dfs(t)) != -1: return u
    vis.discard(s); return -1
for i in range(v):
    while True:
        p, vis = [-1]*v, set()
        d = dfs(i)
        if d == -1: break
        path, d = [d[0]], d[1]
        while d != path[0]: path.append(d); d = p[d]
        path.append(path[0])
        c = min(g[path[j+1]][path[j]] for j in range(len(path)-1))
        for j in range(len(path)-1):
            g[path[j+1]][path[j]] -= c
            if g[path[j+1]][path[j]] == 0: g[path[j+1]].pop(path[j])
el = [(i, j, g[i][j]) for i in range(v) for j in g[i]]
print(len(el))
for i in el: print(*i)