from heapq import *
n, m, s, d = map(int, input().split())
c = [*map(int, input().split())]; o = c.copy()
pq = [(c[i], i) for i in range(s)]
heapify(pq)
for _ in range(n):
    while True:
        q, i = heappop(pq)
        if c[i] != d: break
    c[i] += 1; heappush(pq, (q, i))
r = [c[i]-o[i] for i in range(s)]
k = 0
for i in range(s):
    if r[i] == 0: k += o[i]
if k < m: print('impossible')
else: print(*r)