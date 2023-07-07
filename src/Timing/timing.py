import sys; input = sys.stdin.readline
from collections import defaultdict
sup = lambda: defaultdict(lambda: 0)

def mul(a, b):
    c = defaultdict(sup)
    for i in a:
        for k in a[i]:
            for j in b[k]: c[i][j] += a[i][k]*b[k][j]
    return c

def pow(mat, n):
    if n == 1: return mat
    if n % 2: return mul(pow(mat, n-1), mat)
    return pow(mul(mat, mat), n//2)

for _ in range(int(input())):
    v, e, t = map(int, input().split())
    g, r, m, d = [[] for _ in range(v)], [*map(int, input().split())], defaultdict(sup), [1]*v
    for _ in range(e):
        a, b, p = map(float, input().split())
        a, b = map(int, (a, b))
        d[a] -= p; m[b][a] = p; g[a].append(b), g[b].append(a)
    for i in range(v): m[i][i] = d[i]
    if t:
        x = defaultdict(sup)
        for i in range(v): x[i][0] = r[i]
        m = mul(pow(m, t), x) if t else x
        r = [m[i][0] for i in range(v)]
    z = r.copy()
    for i in range(v): z[i] += sum(r[j] for j in g[i])
    print(round(min(z), 6))