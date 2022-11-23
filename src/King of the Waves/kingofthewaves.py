import sys
from collections import deque

n = int(input())
g = {}
i = 0
for line in sys.stdin:
    line = line.strip()
    for j in range(n):
        if line[j] == '1':
            if i not in g:
                g[i] = [j]
            else:
                g[i].append(j)
    i += 1
q = deque([0])
vis = set()
res = []
while q:
    u = q.popleft()
    if u in vis: continue
    vis.add(u)
    res.append(u)
    if u in g:
        for v in g[u]:
            q.append(v)
if len(vis) != n:
    print('impossible')
else:
    print(*(res[:0:-1] + [0]))