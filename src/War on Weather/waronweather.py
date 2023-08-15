import sys; input = sys.stdin.readline
from math import *
while True:
    k, m = map(int, input().split())
    if k == m == 0: break
    s = [[*map(float, input().split())] for _ in range(k)]
    t = [[*map(float, input().split())] for _ in range(m)]
    ans = 0
    for tx, ty, tz in t:
        for sx, sy, sz in s:
            if (sx-tx)*tx + (sy-ty)*ty + (sz-tz)*tz >= 0: ans += 1; break
    print(ans)