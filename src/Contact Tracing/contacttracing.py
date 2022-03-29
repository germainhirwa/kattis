from collections import deque
import sys

v, d = map(int, input().split())
q = None
g = []
se = []

for line in sys.stdin:
    if not q:
        q = list(map(int, line.split()))
        continue
    g.append([])
    s, e = map(int, line.split())
    se.append((s, e, len(se)))
se.sort(key=lambda x: x[1])

for i in range(len(se)):
    s, e, idx = se[i]
    cp = i - 1
    while cp >= 0 and se[cp][1] >= s:
        g[se[cp][2]].append(idx)
        g[idx].append(se[cp][2])
        cp -= 1

vis = [False] * v
for k in range(1, len(q)):
    vis[q[k] - 1] = True
q = deque(map(lambda x: (x - 1, 0), q))
q.popleft()

while q:
    u, dp = q.popleft()
    if dp == d:
        break
    for n in g[u]:
        if not vis[n]:
            vis[n] = True
            q.append((n, dp + 1))
for i in range(v):
    if vis[i]:
        print(i + 1, end=' ')