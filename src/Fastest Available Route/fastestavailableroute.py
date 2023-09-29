import sys; input = sys.stdin.readline
from collections import *
h, w, s = map(int, input().split()); q = deque()
m = [input().strip() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if m[i][j] == '@': q.append((0, i, j))
        elif m[i][j] == '$': ti, tj = i, j
v = [[0]*w for _ in range(h)]; k = ((0, -1), (0, 1), (1, 0), (-1, 0))
while q:
    d, i, j = q.popleft()
    if v[i][j]: continue
    if i==ti and j==tj: print('Your destination will arrive in', s*d, 'meters'), exit(0)
    v[i][j] = 1
    for di, dj in k:
        if 0<=i+di<h and 0<=j+dj<w and m[i+di][j+dj] in '.$': q.append((d+1, i+di, j+dj))