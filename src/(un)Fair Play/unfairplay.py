import sys; input = sys.stdin.readline
from collections import deque
INF = 1e18

def BFS(s, t):
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for idx in AL[u]:
            v, cap, flow = EL[idx]
            if cap > flow and d[v] == -1:
                d[v] = d[u]+1
                q.append(v)
    return d[t] != -1

def DFS(u, t, f=INF):
    if u == t or f == 0: return f
    for i in range(last[u], len(AL[u])):
        last[u] = i
        v, cap, flow = EL[AL[u][i]]
        if d[v] != d[u]+1: continue
        pushed = DFS(v, t, min(f, cap - flow))
        if pushed:
            EL[AL[u][i]][2] += pushed
            EL[AL[u][i]^1][2] -= pushed
            return pushed
    return 0

def add_edge(u, v, capacity):
    EL.append([v, capacity, 0]), AL[u].append(len(EL)-1), EL.append([u, 0, 0]), AL[v].append(len(EL)-1)

EL = []
while True:
    try: v, E = map(int, input().split())
    except: break
    s = [*map(int, input().split())]
    u, m = [], []
    for _ in range(E):
        i, j = map(int, input().split())
        if i == v or j == v: s[-1] += 2
        else: u.append((i-1, j-1))
        m.append((i-1, j-1))
    U = len(u)
    V = v + U + 2
    source, sink = V-2, V-1
    AL = [[] for _ in range(V)]; EL.clear()
    for j in range(U): add_edge(source, j, 2)
    for j, (a, b) in enumerate(u): add_edge(j, U+a, 2), add_edge(j, U+b, 2)
    for j in range(U, U+v): add_edge(j, sink, s[-1]-(j!=U+v-1)), add_edge(source, j, s[j-U])
    mf, d = 0, [-1]*V
    while BFS(source, sink):
        last = [0]*V
        f = DFS(source, sink)
        while f: mf += f; f = DFS(source, sink)
        d = [-1]*V
    if mf != sum(s)+2*U: print('NO'), input(); continue
    r, x = [], 0
    for i, j in m:
        if i == v-1: r.append(0)
        elif j == v-1: r.append(2)
        else: r.append(EL[AL[x][2]][2]); x += 1
    print(*r), input()