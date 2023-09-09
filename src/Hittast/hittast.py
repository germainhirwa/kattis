import sys; input = sys.stdin.readline
from heapq import *
from array import *
n, m = map(int, input().split())
l = [*map(int, input().split())]
ga, gb = [{} for _ in range(n)], [{} for _ in range(n)]
for _ in range(m):
    u, v, a, b = map(int, input().split())
    ga[u-1][v-1] = ga[v-1][u-1] = a
    gb[u-1][v-1] = gb[v-1][u-1] = b

INF = 10**9; DA = array('i', [INF]*n); DB = array('i', [INF]*n)
DA[0] = 0; DB[-1] = 0
pq = [0]
while pq:
    dv = heappop(pq); dd, vv = dv//n, dv%n
    if dd != DA[vv]: continue
    for nn in ga[vv]:
        if DA[nn] > (new:=dd+ga[vv][nn]): DA[nn] = new; heappush(pq, new*n+nn)
pq = [n-1]
while pq:
    dv = heappop(pq); dd, vv = dv//n, dv%n
    if dd != DB[vv]: continue
    for nn in gb[vv]:
        if DB[nn] > (new:=dd+gb[vv][nn]): DB[nn] = new; heappush(pq, new*n+nn)
print(min(DA[i]+DB[i]+l[i] for i in range(n)))