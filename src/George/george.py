from heapq import *
import sys

v, e = map(int, input().split())
a, b, k, g = map(int, input().split())
gg = list(map(int, input().split()))

graph = {}
for line in sys.stdin:
    aa, bb, ll = map(int, line.split())
    if aa not in graph:
        graph[aa] = {}
    if bb not in graph:
        graph[bb] = {}
    graph[aa][bb] = graph[bb][aa] = ll

block = {}
t = -k
for i in range(1, len(gg)):
    block[(gg[i], gg[i - 1])] = block[(gg[i - 1], gg[i])] = (t, t + graph[gg[i]][gg[i - 1]])
    t += graph[gg[i]][gg[i - 1]]

D = [float('inf')] * (v + 1)
D[a] = 0
pq = [(0, a)]

while pq:
    dd, vv = heappop(pq)
    if dd == D[vv] and vv in graph:
        for nn in graph[vv]:
            w = graph[vv][nn]
            if (vv, nn) in block:
                lo, hi = block[(vv, nn)]
                if lo <= dd <= hi:
                    w += hi - dd
            if D[nn] > dd + w:
                D[nn] = dd + w
                heappush(pq, (D[nn], nn))
print(D[b])