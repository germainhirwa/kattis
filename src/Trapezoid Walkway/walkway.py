from heapq import *
import sys; input = sys.stdin.readline
while True:
    n = int(input())
    if not n: break
    g = [{} for _ in range(2*n+2)]
    d = []
    for i in range(n):
        a, b, h = map(int, input().split())
        g[2*i][2*i+1] = g[2*i+1][2*i] = (a+b)/100*h
        d.append(a), d.append(b)
    d.extend(map(int, input().split()))
    if d[-1] == d[-2]: print(0); continue
    D = {2*n: 0}
    pq = [(0, 2*n)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(2):
                for l in range(2):
                    if d[2*i+k] == d[2*j+l]: g[2*i+k][2*j+l] = g[2*j+l][2*i+k] = 0
        for j in range(2):
            for k in range(2):
                if d[2*i+j] == d[2*n+k]: g[2*i+j][2*n+k] = g[2*n+k][2*i+j] = 0
    while pq:
        dd, vv = heappop(pq)
        if dd == D[vv]:
            for nn in g[vv]:
                if nn not in D or D[nn] > dd + g[vv][nn]:
                    D[nn] = dd + g[vv][nn]
                    heappush(pq, (D[nn], nn))
    print(D[2*n+1])