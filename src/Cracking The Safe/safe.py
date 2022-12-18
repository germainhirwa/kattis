import sys
from collections import deque

m = []
for _ in range(3):
    m.extend(input().split())
s = tuple(map(int, m))

q = deque([(s, 0)])
v = set()
while q:
    m, d = q.popleft()
    if sum(m) == 0:
        print(d)
        sys.exit(0)
    if m in v: continue
    v.add(m)
    for r in range(3):
        for c in range(3):
            t = list(m)
            for i in range(3):
                t[3*r+i] += 1
                t[3*i+c] += 1
                t[3*r+i] %= 4
                t[3*i+c] %= 4
            t[3*r+c] -= 1
            t[3*r+c] %= 4
            q.append((tuple(t), d+1))
print(-1)