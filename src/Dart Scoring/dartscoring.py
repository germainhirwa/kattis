from math import *

def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])

def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) > (r[0]-p[0])*(q[1]-p[1])

def chull(pts):
    if len(pts) < 3: return pts
    pts, n = sorted(pts), len(pts)
    upper, lower = pts[:2], pts[-1:-3:-1]
    for i in range(2, n):
        while len(upper) > 1 and not ccw(upper[-2], upper[-1], pts[i]): upper.pop()
        upper.append(pts[i])
    for i in range(n-2, -1, -1):
        while len(lower) > 1 and not ccw(lower[-2], lower[-1], pts[i]): lower.pop()
        lower.append(pts[i])
    return upper[:-1] + lower[:-1]

import sys
for l in sys.stdin:
    pts = [[]]
    for i in map(float, l.split()):
        pts[-1].append(i)
        if len(pts[-1]) == 2: pts[-1] = tuple(pts[-1]); pts.append([])
    pts.pop()
    n, s = len(pts), 0
    ch = chull(pts)
    ch.append(ch[0])
    for i in range(len(ch)-1): s += dist(ch[i], ch[i+1])
    print(100*n/(1+s))