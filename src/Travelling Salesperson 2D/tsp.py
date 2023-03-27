from random import randint, random, shuffle
from math import exp, hypot
import sys
sys.setrecursionlimit(1005)

def swap(s, m, n):
    i, j = min(m, n), max(m, n)
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

def cost(G, s):
    l = 0
    for i in range(N-1): l += G[s[i]][s[i+1]]
    l += G[s[-1]][s[0]]
    return l

def mst(G):
    st = []
    a, b = [(1e9, i) for i in range(N)], [1]*N
    a[0] = (0, 0)
    while len(st) != N:
        mi, mv = 0, a[0]
        for i in range(1, N):
            if a[i] < mv: mi, mv = i, a[i]
        st.append((mi, mv))
        a[mi], b[mi] = (1e9, mi), 0
        for w in range(N):
            if b[w] and a[w] > (G[mi][w], mi):
                a[w] = (G[mi][w], mi)
    g = [[] for _ in range(N)]
    for t in st[1:]: g[t[1][1]].append(t[0]), g[t[0]].append(t[1][1])
    return g

def tsp_sa(G, s=None, lim=250_000):
    # simulated annealing
    if s == None: s = list(range(N))
    c = cost(G, s)
    ntrial = 1

    # hyperparameter
    T = 10_000_000
    alpha = 0.99

    shuffle(s)
    while ntrial <= lim:
        n = randint(0, N-1)
        while True:
            m = randint(0, N-1)
            if n != m: break
        swap(s, m, n)
        c1 = cost(G, s)
        if c1 < c or random() < exp((c-c1)/T): c = c1
        else: swap(s, m, n)
        T = alpha*T
        ntrial += 1
    return s

def tsp_mst(G):
    g = mst(G)
    st, vis = [], {0}
    def dfs(u):
        st.append(u)
        for i in g[u]:
            if i not in vis: vis.add(i), dfs(i)
    dfs(0)
    return st

def tsp_chris(G):
    # a work in progress, expected to give better than MST when it's done
    g = mst(G)
    odd = [i for i in range(N) if len(g[i]) % 2]

    # greedy maximum matching :)
    el = []
    for i in range(len(odd)):
        for j in range(i+1, len(odd)): el.append((odd[i], odd[j], G[odd[i]][odd[j]]))
    el.sort(key=lambda x: -x[-1])
    m, vis = [], set()
    for u, v, _ in el:
        if len(m) == len(odd) // 2: break
        if u in vis or v in vis: continue
        m.append((u, v)), vis.add(u), vis.add(v)
    for u, v in m: g[u].append(v), g[v].append(u)

    # eulerian circuit using hierholzer's
    a, idx, st = [], [0]*N, [0]
    while st:
        u = st[-1]
        if idx[u] < len(g[u]):
            st.append(g[u][idx[u]])
            idx[u] += 1
        else:
            a.append(u)
            st.pop()
    s, vis = [], set()
    for i in a[::-1]:
        if i in vis: continue
        vis.add(i), s.append(i)
    return s

def L1(x, y):
    return abs(x) + abs(y)

def L2(x, y):
    return round(hypot(x, y))

N = int(input())
if N == 1: print(0)
else:
    p = [list(map(float, input().split())) for _ in range(N)]
    G = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N): G[i][j] = G[j][i] = L2(p[i][0]-p[j][0], p[i][1]-p[j][1])
    s = tsp_sa(G, tsp_mst(G))
    for i in s: print(i)
    #print('Initial cost:', cost(G, list(range(N))))
    #print('Cost:'.ljust(13), cost(G, s))