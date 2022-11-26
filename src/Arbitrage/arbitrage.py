INF = 1e9
def fw(g, v):
    D = [[g[i][j] if i in g and j in g[i] else INF for j in range(v)] for i in range(v)]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

from math import log
import sys
n, c, m = -1, [], -1
for line in sys.stdin:
    if n == -1:
        n = int(line)
    elif c == []:
        c = line.strip().split()
        h = dict(map(reversed, enumerate(c)))
        g = {}
    elif m == -1:
        m = int(line)
        if m == 0:
            print('Ok')
            n, c, m = -1, [], -1
    else:
        a, b, r = line.split()
        r1, r2 = map(int, r.split(':'))
        u, v = h[a], h[b]
        if u not in g: g[u] = {}
        g[u][v] = log(r1/r2)
        m -= 1
        if m == 0:
            D = fw(g, n)
            ok = 1
            for i in range(n):
                if D[i][i] < 0:
                    ok = 0
                    break
            print(['Arbitrage', 'Ok'][ok])
            n, c, m = -1, [], -1