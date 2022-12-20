import sys
from collections import deque
f, s, g, u, d = map(int, input().split())
q = deque([(s, 0)])
vis = set()
while q:
    m, t = q.popleft()
    if m == g:
        print(t)
        sys.exit(0)
    if m in vis: continue
    vis.add(m)
    if m+u <= f:
        q.append((m+u, t+1))
    if m-d >= 0:
        q.append((m-d, t+1))
print('use the stairs')