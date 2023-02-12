import sys
from heapq import *

n = int(input())
items = list(map(int, input().split()))
input()
g = [{} for _ in range(n)]
for line in sys.stdin:
    a, b, d = map(int, line.split())
    a -= 1
    b -= 1
    g[a][b] = g[b][a] = d

def dijkstra(D, s, t):
    D[s] = (0, 0)
    pq = [(0, 0, s)]
    while pq:
        dd, pp, vv = heappop(pq)
        if dd == D[vv][0]:
            for nn in g[vv]:
                if nn not in D or D[nn] >= (dd + g[vv][nn], pp - items[vv]):
                    D[nn] = (dd + g[vv][nn], pp - items[vv])
                    heappush(pq, (*D[nn], nn))
    if t not in D: return print('impossible')
    dis, pick = D[t]
    print(dis, -pick+items[t])

dijkstra({}, 0, n-1)