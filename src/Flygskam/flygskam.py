from math import *
from heapq import *
import sys; input = sys.stdin.readline
N, E = map(int, input().split())
s, t = input().strip().split()
G = [{} for _ in range(N)]
C = []; rev = {}
for _ in range(N):
    f, lat, lon = input().split()
    rev[f] = len(rev); C.append((float(lat)*pi/180, float(lon)*pi/180))
s, t = rev[s], rev[t]
for i in range(E):
    a, b = input().strip().split(); a, b = rev[a], rev[b]
    G[a][b] = G[b][a] = 6381*(acos(sin(C[a][0])*sin(C[b][0])+cos(C[a][0])*cos(C[b][0])*cos(abs(C[a][1]-C[b][1]))))+100
D = {}
D[s] = 0
pq = [(0, s)]
while pq:
    dd, vv = heappop(pq)
    if dd == D[vv]:
        for nn in G[vv]:
            if nn not in D or D[nn] > dd + G[vv][nn]:
                D[nn] = dd + G[vv][nn]
                heappush(pq, (D[nn], nn))
print(D[t] if t in D else -1)