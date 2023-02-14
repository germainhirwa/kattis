def fw(g, v, s, t):
    D = [[1 if j in g[i] else 0 for j in range(v)] for i in range(v)]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                D[i][j] |= D[i][k] * D[k][j]
    return D[s][t]

for _ in range(int(input())):
    n = int(input())
    g = [set() for _ in range(n+2)]
    pts = []
    for i in range(n+2):
        x, y = map(int, input().split())
        pts.append((x, y))
    for i in range(n+2):
        for j in range(i+1, n+2):
            (x1, y1), (x2, y2) = pts[i], pts[j]
            if abs(x1-x2) + abs(y1-y2) <= 1000:
                g[i].add(j)
                g[j].add(i)
    print(['sad', 'happy'][fw(g, n+2, 0, n+1)])