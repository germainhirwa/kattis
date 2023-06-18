from math import *
from collections import deque

# somehow passed, but will not if there are 3+ clustered points :)
for _ in range(int(input())):
    n, d = map(int, input().split())
    pts = []
    for _ in range(n):
        x, y = map(int, input().split())
        if x**2 + y**2 > d**2: pts.append((x, y, atan2(y, x)))
    pts.sort(key=lambda x: x[2])
    ans = 1e9
    for i in range(len(pts)):
        pts2 = deque(pts[i:] + pts[:i])
        pts2.append(pts2[0])
        lines = []
        while len(pts2) >= 2:
            (x1, y1, a1), (x2, y2, a2) = pts2.popleft(), pts2.popleft()
            am = atan2(y1+y2, x1+x2)
            if round(abs(x1*sin(am)-y1*cos(am)), 9) <= d and round(abs(x2*sin(am)-y2*cos(am)), 9) <= d:
                lines.append(am)
                continue
            else:
                lines.append(a1)
                pts2.appendleft((x2, y2, a2))
        ans = min(ans, len(set(lines)))
    print(ans)