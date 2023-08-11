import sys
from math import *
for l in sys.stdin:
    p = [*map(int, l.split())][1:]; n = len(p)//2
    if not p: break
    pp = []
    for t in range(n-2):
        s = n-t; b = (1e9, -1)
        for i in range(s):
            x, y = p[2*i], p[2*i+1]
            x1, y1 = p[2*((i-1)%s)], p[2*((i-1)%s)+1]
            x2, y2 = p[2*((i+1)%s)], p[2*((i+1)%s)+1]
            dx1, dy1 = x1-x, y1-y
            dx2, dy2 = x2-x, y2-y
            a = acos((dx1*dx2+dy1*dy2)/hypot(dx1,dy1)/hypot(dx2,dy2))
            b = min(b, (a, i))
        pp.append((p.copy(), b[0])); p.pop(2*b[1]), p.pop(2*b[1])
    pos = 0
    while pos < len(pp)-1:
        if pp[pos][1] > pp[pos+1][1]: break
        pos += 1
    p = pp[pos][0]
    print(len(p)//2, *p)