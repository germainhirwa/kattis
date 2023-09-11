import sys; input = sys.stdin.readline
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

R, C = map(int, input().split())
V = R+C+2
source, sink = V-2, V-1
EL, AL = [], [[] for _ in range(V)]
def add(u, v, capacity=1): EL.append([v, capacity, 0]), AL[u].append(len(EL)-1), EL.append([u, 0, 0]), AL[v].append(len(EL)-1)

ans = 0; rowmax = [0]*R; colmax = [0]*C
arr = [[*map(int, input().split())] for _ in range(R)]
for i in range(R):
    for j, e in enumerate(arr[i]):
        rowmax[i] = max(rowmax[i], e)
        colmax[j] = max(colmax[j], e)
        ans += e-(e>0)
for i in range(R):
    add(source, i); ans -= max(0, rowmax[i]-1)
    for j in range(C):
        if rowmax[i] == colmax[j] and arr[i][j]: add(i, R+j)
for i in range(C):
    ans -= max(0, colmax[i]-1); add(R+i, sink)

d = [-1]*V
while BFS(source, sink):
    last = [0]*V
    f = DFS(source, sink)
    while f: f = DFS(source, sink)
    d = [-1]*V
for t in AL[source]:
    if EL[t][2]: ans += max(0, rowmax[EL[t][0]]-1)
print(ans)