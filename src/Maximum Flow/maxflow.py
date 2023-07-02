from collections import deque

INF = float('inf')

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

import sys
V, E, source, sink = map(int, input().split())
EL, AL = [], [[] for _ in range(V)]
for l in sys.stdin:
    u, v, capacity = map(int, l.split())
    EL.append([v, capacity, 0]), AL[u].append(len(EL)-1), EL.append([u, 0, 0]), AL[v].append(len(EL)-1)

mf = 0
d = [-1]*V
while BFS(source, sink):
    last = [0]*V
    f = DFS(source, sink)
    while f: mf += f; f = DFS(source, sink)
    d = [-1]*V

used = []
for i in range(E):
    if EL[2*i][2] == 0: continue
    used.append((EL[2*i+1][0], EL[2*i][0], EL[2*i][2]))
print(V, mf, len(used))
for i in used: print(*i)