from sys import stdin; input = stdin.readline
def solve(t):
    v, e = map(int, input().split())
    g, g2, el = [[] for _ in range(v)], [[] for _ in range(v)], []
    for _ in range(e):
        a, b = map(int, input().split())
        g[a].append(b), g2[b].append(a), el.append((a, b))
    def count_scc():
        top, vis, scc = [], set(), 0
        def DFS(s, add):
            vis.add(s)
            a = g2 if add else g
            for v in a[s]:
                if v not in vis: DFS(v, add)
            if add: top.append(s)
        for i in range(v):
            if i not in vis: DFS(i, True)
        vis.clear()
        for i in top[::-1]:
            if i not in vis: scc += 1; DFS(i, False)
        if scc == 1: return True
    if count_scc() == 1: print(f'Case {t}: valid'); return t+1
    for i, j in el:
            g[i].remove(j), g2[j].remove(i), g2[i].append(j), g[j].append(i)
            if count_scc() == 1: print(f'Case {t}: {i} {j}'); return t+1
            g2[i].remove(j), g[j].remove(i), g[i].append(j), g2[j].append(i)
    print(f'Case {t}: invalid'); return t+1
t = 1
while True:
    try: t = solve(t)
    except: break