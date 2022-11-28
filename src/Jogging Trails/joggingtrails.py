import sys

INF = float('inf')

def fw(g, v):
    D = [[min(g[i][j]) if i in g and j in g[i] else INF for j in range(v)] for i in range(v)]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

# https://stackoverflow.com/questions/5360220/how-to-split-a-list-into-pairs-in-all-possible-ways
def all_pairs(lst):
    if len(lst) < 2:
        yield []
        return
    if len(lst) % 2:
        for i in range(len(lst)):
            for result in all_pairs(lst[:i] + lst[i+1:]):
                yield result
    else:
        for i in range(1, len(lst)):
            pair = (lst[0], lst[i])
            for rest in all_pairs(lst[1:i] + lst[i+1:]):
                yield [pair] + rest

def cpp(g, deg):
    D = fw(g, len(deg))
    odd = [i for i in range(len(deg)) if deg[i] % 2]
    add = INF
    for pairings in all_pairs(odd):
        add = min(add, sum(D[i][j] for i, j in pairings))
    e = 0
    for i in g:
        for j in g[i]:
            e += sum(g[i][j])
    return e // 2 + add

n, m = map(int, input().split())
g, deg = {}, [0]*n
for line in sys.stdin:
    m -= 1
    u, v, w = map(int, line.split())
    u -= 1
    v -= 1
    for _ in range(2):
        if u not in g:      g[u] = {}
        if v not in g[u]:   g[u][v] = []
        g[u][v].append(w)
        deg[u] += 1
        u, v = v, u
    if m == 0:
        print(cpp(g, deg))
        try:
            n, m = map(int, input().split())
            g, deg = {}, [0]*n
        except:
            break