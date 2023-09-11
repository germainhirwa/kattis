from collections import *
from array import *
import sys; input = sys.stdin.readline
n, k, m = map(int, input().split()); k -= 1
g = [array('i') for _ in range(n)]; d = array('i', [0]*n)
for _ in range(m):
    a, b = map(int, input().split()); a -= 1; b -= 1
    g[a].append(b), g[b].append(a); d[a] += 1; d[b] += 1
q = deque([i for i in range(n) if d[i] < 2])
while q:
    u = q.popleft()
    if u == k: print('YES'), exit(0)
    for v in g[u]:
        d[v] -= 1
        if d[v] == 1: q.append(v)
print('NO')