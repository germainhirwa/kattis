from collections import deque
n, m  = map(int, input().split())
g, g2, q = [[] for _ in range(n)], [[] for _ in range(n)], deque([(0, 1)])
for _ in range(m):
    a, b = map(int, input().split())
    [g2, g][a>0][abs(a)-1].append(b-1)
v, s = {(0, 1)}, set()
while q:
    u, c = q.popleft()
    if g2[u]:
        tup = (g2[u][0], c)
        if tup not in v: v.add(tup), q.append(tup)
    else:
        s.add(u)
    if c:
        for i in g[u]:
            tup = (i, 0)
            if tup not in v: v.add(tup), q.append(tup)
print(len(s))