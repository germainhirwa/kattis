import sys
n = int(input())
arr = []
for line in sys.stdin:
    arr.append(int(line))

m = max(arr)
al = []
for _ in range(n):
    al.append([])
s = []

for r in (range(n), range(n - 1, -1, -1)):
    stack = []
    for i in r:
        if arr[i] == m:
            s.append(i)
        if stack:
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            if stack:
                al[stack[-1]].append(i)
        stack.append(i)

from collections import deque
depth = [n] * n

# Multi-source BFS
r = [False] * n
q = deque((i, 0) for i in s)
while q:
    v, d = q.popleft()
    if r[v]:
        continue
    depth[v] = d
    r[v] = True
    for nx in al[v]:
        if not r[nx]:
            q.append((nx, d + 1))
print(*depth)