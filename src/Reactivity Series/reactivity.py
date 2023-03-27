import sys
from collections import deque

n, k = map(int, input().split())
g, indeg = [set() for _ in range(n)], [0]*n
for line in sys.stdin:
    a, b = map(int, line.split())
    g[a].add(b)
    indeg[b] += 1

q = deque()
for v in range(n):
    if indeg[v] == 0: q.append(v)
top = []
while q:
    u = q.popleft()
    top.append(u)
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)

back = False
for i in range(1, len(top)):
    if top[i] in g[top[i-1]]: continue
    back = True; break

if back: print('back to the lab')
else: print(*top)