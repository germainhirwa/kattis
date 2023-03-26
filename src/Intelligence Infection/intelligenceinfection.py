from collections import deque
import sys
s, e, c = map(int, input().split())
g = [[] for _ in range(s)]
for line in sys.stdin:
    if c != 0:
        c -= 1
        a, b = map(int, line.split())
        g[b].append(a)
    else:
        ee = list(map(int, line.split()))
        vis, q = set(ee), deque(ee)

while q:
    for v in g[q.popleft()]:
        if v not in vis: q.append(v), vis.add(v)
private = len(vis) - e

g2 = {}
for i in range(s):
    if i not in vis:
        if i not in g2: g2[i] = []
        for j in g[i]:
            if j not in vis:
                if j not in g2: g2[j] = []
                g2[j].append(i)

public, top, vis = 0, [], set()
def DFS(s, a=1):
    t = [2*s]
    while t:
        ub = t.pop()
        u, b = ub//2, ub%2
        if b and a: top.append(u)
        elif u not in vis:
            vis.add(u), t.append(2*u+1)
            for v in g2[u]:
                if v not in vis: t.append(2*v)
    return 1
for i in g2:
    if i not in vis: DFS(i)
vis.clear()

for i in top[::-1]:
    if i not in vis: public += DFS(i, 0)
print(public+private)