from heapq import *
import sys; input = sys.stdin.readline
A, H = map(int, input().split())
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m): e, b, a, h = map(int, input().split()); g[e-1].append((b-1, a, h))

def exchange(h, a2, h2):
    return h-(h2//A+bool(h2%A)-1)*a2

D = [1e9]*n
D[0] = -H
pq = [(-H, 0)]
while pq:
    dd, vv = heappop(pq)
    if dd == D[vv]:
        for nn, a, h in g[vv]:
            rest = -exchange(-dd, a, h)
            if rest >= 0: continue
            if D[nn] > rest: D[nn] = rest; heappush(pq, (rest, nn))
if D[n-1] >= 0: print('Oh no')
else: print(-D[n-1])