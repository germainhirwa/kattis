import sys

g = {}
n, m = map(int, input().split())
for line in sys.stdin:
    m -= 1
    b, ag = line.strip().split()
    b = int(b)
    for i in range(n):
        for j in range(i+1, n):
            x, y = ord(ag[i])-65, ord(ag[j])-65
            if x not in g: g[x] = {}
            if y not in g[x]: g[x][y] = 0
            g[x][y] += b
    if m == 0: break
g2 = {}
for i in g:
    for j in g[i]:
        x = g[i] if i in g else {}
        x2 = x[j] if j in x else 0
        y = g[j] if j in g else {}
        y2 = y[i] if i in y else 0
        if x2 > y2:
            if i not in g2: g2[i] = []
            g2[i].append(j)

def dfs(u):
    if vis[u]: return
    vis[u] = 1
    if u in g2:
        for v in g2[u]: dfs(v)

win = {}
for i in ag:
    vis = [0]*26
    dfs(ord(i)-65)
    win[i] = sum(vis) == n
for i in sorted(win):
    print(f"""{i}: can{"'t"*(1-win[i])} win""")