from collections import deque

v, e = map(int, input().split())
arr = list(map(int, input().split()))
g = {}
indeg = [0]*v
for _ in range(e):
    i, j, w = map(int, input().split())
    if j not in g: g[j] = {}
    g[j][i] = w
    indeg[i] += 1
q = deque()
for i in range(v):
    if not indeg[i]: q.append(i)
while q:
    u = q.popleft()
    if u in g:
        for u2 in g[u]:
            indeg[u2] -= 1
            if not indeg[u2]: q.append(u2)
            arr[u2] += arr[u]*g[u][u2]
print(*arr)