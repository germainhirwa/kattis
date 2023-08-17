from math import *
import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    p = [[*map(int, input().split())] for _ in range(n)]
    best = 0
    for i in range(1<<n):
        c = []; a = 0
        for j in range(n):
            xx, yy, rr = p[j]
            if i&(1<<j):
                ok = True
                for x, y, r in c:
                    if hypot(x-xx, y-yy)<=r+rr: ok = False; break
                if ok: c.append(p[j]); a += rr**2
        best = max(a, best)
    print(best)