import sys

INF = float('inf')
def fw(D, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

n, m = -1, -1
for line in sys.stdin:
    if n == -1:
        n = int(line)
        pts, D = [], [[INF for _ in range(n)] for _ in range(n)]
        for i in range(n): D[i][i] = 0
    elif n != 0:
        x, y = map(int, line.split())
        pts.append((x, y))
        n -= 1
    elif n == 0 and m == -1:
        m = int(line)
    else:
        u, v = map(int, line.split())
        (x1, y1), (x2, y2) = pts[u], pts[v]
        D[u][v] = D[v][u] = ((x1-x2)**2 + (y1-y2)**2)**0.5
        m -= 1
        if m == 0:
            n = len(pts)
            fw(D, n)
            t, memo = 0, {}
            for i in range(n):
                for j in range(i+1, n):
                    t += D[i][j]
            best = (t, -1, 1)
            for i in range(n):
                x1, y1 = pts[i]
                for j in range(i+1, n):
                    x2, y2 = pts[j]
                    memo.clear()
                    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
                    D[i][j], memo[(i, j)] = d, D[i][j]
                    t2 = 0
                    for i2 in range(n):
                        for j2 in range(i2+1, n):
                            new = d + min(D[i2][i] + D[j][j2], D[i2][j] + D[i][j2])
                            if D[i2][j2] > new: D[i2][j2], memo[(i2, j2)] = new, D[i2][j2]
                            t2 += D[i2][j2]
                    best = min(best, (t2, i, j))
                    for (i2, j2), p in memo.items(): D[i2][j2] = p
            if best[1]*best[2] != -1:
                src, dest = best[1:]
                print(f'adding {src} {dest} reduces {t} to {best[0]}')
            else:
                print(f'no addition reduces {t}')
            n, m = -1, -1