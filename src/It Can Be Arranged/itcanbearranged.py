import sys; input = sys.stdin.readline
from collections import deque
from math import ceil

INF = float('inf')
def get_flow(C):
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
    def add(u, v, capacity):
        EL.append([v, capacity, 0]), AL[u].append(len(EL)-1), EL.append([u, 0, 0]), AL[v].append(len(EL)-1)
    EL, AL = [], [[] for _ in range(V)]
    add(2*N+1, 2*N+2, C)
    for i, (_, _, S) in enumerate(T): add(source, i, sm:=ceil(S/M)); add(i+N, sink, sm), add(i, 2*N+1, INF), add(2*N+2, i+N, INF)
    for i in range(N-1):
        for j in range(i+1, N):
            if T[i][1] + clean[i][j] < T[j][0]: add(i, j+N, INF)
            elif T[j][1] + clean[j][i] < T[i][0]: add(j, i+N, INF)
    mf = 0
    d = [-1]*V
    while BFS(source, sink):
        last = [0]*V
        f = DFS(source, sink)
        while f: mf += f; f = DFS(source, sink)
        d = [-1]*V
    return mf

for t in range(int(input())):
    N, M = map(int, input().split())
    T = [[*map(int, input().split())] for _ in range(N)]
    clean = [[*map(int, input().split())] for _ in range(N)]
    V = 2*N+4
    source, sink = 2*N, 2*N+3
    ss = sum(ceil(i[2]/M) for i in T)
    lo, hi = 1, ss
    while lo < hi:
        mid = (lo+hi)//2
        if get_flow(mid) == ss: hi = mid
        else: lo = mid+1
    print(f'Case {t+1}:', hi)