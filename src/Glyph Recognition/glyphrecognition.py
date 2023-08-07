from math import *

def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def norm(a):
    return hypot(a[0], a[1])

def angle(a, o, b):
    v1, v2 = (a[0]-o[0], a[1]-o[1]), (b[0]-o[0], b[1]-o[1])
    return acos(round(dot(v1, v2)/(norm(v1)*norm(v2)), 15))

def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) > (r[0]-p[0])*(q[1]-p[1])

def pip(p, poly):
    if not poly: return False
    for i in range(len(poly)-1):
        if abs(dist(poly[i], p) + dist(p, poly[i+1]) - dist(poly[i], poly[i+1])) < 1e-12: return True
    s = 0
    for i in range(len(poly)-1): s += (2*ccw(p, poly[i], poly[i+1])-1) * angle(poly[i], p, poly[i+1])
    return abs(abs(s) - 2*pi) < 8e-9

def ngon(n):
    p = [(1, 0)]; a = 2*pi/n
    for i in range(1, n): p.append((cos(i*a), sin(i*a)))
    p.append((1, 0)); return p

import sys; input = sys.stdin.readline
n = int(input())
pts = [[*map(int, input().split())] for _ in range(n)]
maxr = max(hypot(x, y) for x, y in pts)
best = (-1, 0)
for k in range(3, 9):
    gon = ngon(k)
    ll, hh = 1e9, -1
    for p in pts:
        lo, hi = 1, 2*maxr
        while abs(lo-hi)>1e-5:
            r = (lo+hi)/2
            pp = 0; poly = [(r*x, r*y) for x, y in gon]
            if pip(p, poly): hi = r
            else: lo = r
        ll = min(ll, r); hh = max(hh, r)
    best = max(best, ((ll/hh)**2, k))
print(*best[::-1])