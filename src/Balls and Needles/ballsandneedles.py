import sys
sys.setrecursionlimit(10**5)
input()
g3d, i3d, g2d, i2d = {}, {}, {}, {}
for line in sys.stdin:
    x1, y1, z1, x2, y2, z2 = map(int, line.split())
    for _ in range(2):
        if (x1, y1, z1) not in g3d:
            g3d[(x1, y1, z1)] = set()
        g3d[(x1, y1, z1)].add((x2, y2, z2))
        if (x2, y2, z2) not in i3d:
            i3d[(x2, y2, z2)] = 0
        i3d[(x2, y2, z2)] += 1
        if (x1, y1) != (x2, y2):
            if (x1, y1) not in g2d:
                g2d[(x1, y1)] = set()
            g2d[(x1, y1)].add((x2, y2))
            if (x2, y2) not in i2d:
                i2d[(x2, y2)] = 0
            i2d[(x2, y2)] += 1
        x1, y1, z1, x2, y2, z2 = x2, y2, z2, x1, y1, z1

def dfs(g, u, prev=None):
    if cyc[0]: return
    if u in vis:
        cyc[0] = True
        return
    vis.add(u)
    if u in g:
        for v in g[u]:
            if v != prev: dfs(g, v, u)
for g, d in [(g3d, 'True'), (g2d, 'Floor')]:
    vis, cyc = set(), [False]
    for i in g:
        if i not in vis:
            dfs(g, i)
    if cyc[0]:
        print(f'{d} closed chains')
    else:
        print(f'No {d.lower()} closed chains')