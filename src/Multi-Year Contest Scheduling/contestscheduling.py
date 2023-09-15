import sys; input = sys.stdin.readline
from datetime import datetime
from heapq import *
z = int(input()); n = int(input())
f = {*(datetime(*map(int, input().split())) for _ in range(n))}
v2 = [[12]]
for y in range(2019, 2019+z):
    m = []; v = []
    for d in range(1, 32):
        if datetime(y, 10, d).weekday() == 0: m.append(d)
    for d in range(1, 32):
        if d == m[1]-3: continue
        dt = datetime(y, 10, d)
        if dt not in f and dt.weekday() == 4: v.append(dt.day)
    v2.append(v)
g = [{} for _ in range(sum(map(len, v2))+1)]; n = len(g); pos = 0
for i in range(z):
    for x, j in enumerate(v2[i]):
        for y, k in enumerate(v2[i+1]):
            g[pos+x][pos+len(v2[i])+y] = (j-k)**2
    pos += len(v2[i])
for i in range(len(v2[z])): g[n-1-len(v2[z])+i][n-1] = 0
INF = float('inf'); D = [INF]*n; D[0] = 0; pq = [(0, 0, None)]; P = [None]*n
while pq:
    dd, vv, p = heappop(pq)
    if dd != D[vv]: continue
    for nn in g[vv]:
        if D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; P[nn] = vv; heappush(pq, (new, nn, vv))
print(D[-1])
path = []; curr = n-1
while curr != None: path.append(curr); curr = P[curr]
path = {*path[1:-1][::-1]}; ptr = 0
for z, i in enumerate(v2):
    for j in i:
        if ptr in path: print(2018+z, 10, str(j).zfill(2))
        ptr += 1