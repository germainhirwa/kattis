from collections import deque
m, n, s0 = map(int, input().split())
ab = [[*map(int, input().split())] for _ in range(n)]
q = deque([(s0, 0)])
vis = set()
while q:
    u, d = q.popleft()
    if u in vis: continue
    vis.add(u)
    if u == 0: print(d), exit(0)
    for a, b in ab: q.append(((u*a+b)%m, d+1))
print(-1)