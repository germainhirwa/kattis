import sys
from collections import deque

r, c, _ = map(int, input().split())
q = set()
vis = [False] * (r*c)
D = [0] * (r*c)
for line in sys.stdin:
    rr, cc = map(int, line.split())
    rr -= 1
    cc -= 1
    vis[rr*c + cc] = True
    q.add((rr*c + cc, 0))

q = deque(q)
while q:
    u, d = q.popleft()
    if u >= c:
        if not vis[u - c]:
            q.append((u - c, d + 1))
            D[u - c] = d + 1
            vis[u - c] = True
    if u < (r-1)*c:
        if not vis[u + c]:
            q.append((u + c, d + 1))
            D[u + c] = d + 1
            vis[u + c] = True
    if u % c > 0:
        if not vis[u - 1]:
            q.append((u - 1, d + 1))
            D[u - 1] = d + 1
            vis[u - 1] = True
    if u % c < c - 1:
        if not vis[u + 1]:
            q.append((u + 1, d + 1))
            D[u + 1] = d + 1
            vis[u + 1] = True
print(max(D) + 1)