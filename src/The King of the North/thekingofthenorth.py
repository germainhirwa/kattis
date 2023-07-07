from collections import deque
import sys; input = sys.stdin.readline
INF = 10**9
r, c = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(r)]

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

def add_edge(u, v, capacity, undir=0):
    EL.append([v, capacity, 0]), AL[u].append(len(EL)-1), EL.append([u, capacity*undir, 0]), AL[v].append(len(EL)-1)

V = 2*r*c+1
sr, sc = map(int, input().split())
source, sink = 2*(sr*c+sc), V-1
EL, AL = [], [[] for _ in range(V)]
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for i in range(r):
    for j in range(c):
        add_edge(2*(i*c+j), 2*(i*c+j)+1, m[i][j], 1)
        for di, dj in delta:
            if 0<=i+di<r and 0<=j+dj<c: add_edge(2*(i*c+j)+1, 2*((i+di)*c+j+dj), 10**9)
            else:                       add_edge(2*(i*c+j)+1, V-1, 10**9)

mf = 0
d = [-1]*V
while BFS(source, sink):
    last = [0]*V
    f = DFS(source, sink)
    while f: mf += f; f = DFS(source, sink)
    d = [-1]*V
print(mf)