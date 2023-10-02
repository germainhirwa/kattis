import sys; input = sys.stdin.readline
from collections import *
n, m = map(int, input().split())
pa, pb = map(int, input().split()); s = [0]*n
g = [[] for _ in range(n)]
for _ in range(m): a, b = map(int, input().split()); g[a].append(b), g[b].append(a)
q = deque([(pa, 0, 1), (pb, 0, 2)])
while q:
    u, d, b = q.popleft()
    if s[u] & b: continue
    s[u] += b
    if s[u] == 3: print(d), exit(0)
    for v in g[u]: q.append((v, d+1, b))