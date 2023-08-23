def intersect(s1, s2):
    (p1, p2), (p3, p4) = s1, s2
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    a, b, c = y2-y1, x1-x2, (y2-y1)*x1 - (x2-x1)*y1
    d, e, f = y4-y3, x3-x4, (y4-y3)*x3 - (x4-x3)*y3
    if a == b == 0: return ((x1, y1) if (x1, y1) == (x3, y3) else None) if d == e == 0 else ((x1, y1) if d*x1 + e*y1 == f and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4) else None)
    elif d == e == 0: return (x3, y3) if a*x3 + b*y3 == c and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2) else None
    else:
        det = b*d-a*e
        if det:
            x, y = (b*f-c*e)/det, (c*d-a*f)/det
            return (x, y) if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4) else None
        else:
            if a*f != c*d or b*f != c*e: return None
            else:
                p, q = min((x1, y1), (x2, y2)), max((x1, y1), (x2, y2))
                r, s = min((x3, y3), (x4, y4)), max((x3, y3), (x4, y4))
                if (p, q) == (r, s):    i1, i2 = p, q
                elif p <= r <= q:       i1, i2 = r, min(q, s)
                elif r <= p <= s:       i1, i2 = p, min(s, q)
                else:                   i1 = i2 = None
                if i1 == i2 and i1 != None: return i1
                else:                       return None # enforce single point

from math import hypot
l = []; K = 10**9
for _ in range(n:=int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    dx, dy = x2-x1, y2-y1
    l.append(((x1-K*dx, y1-K*dy), (x2+K*dx, y2+K*dy)))
best = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        if not (t1:=intersect(l[i], l[j])): continue
        x1, y1 = t1
        for k in range(j+1, n):
            t2, t3 = intersect(l[i], l[k]), intersect(l[j], l[k])
            if t2 == None or t3 == None: continue
            x2, y2 = t2; x3, y3 = t3
            best = max(best, hypot(x1-x2, y1-y2)+hypot(x2-x3, y2-y3)+hypot(x3-x1, y3-y1))
print('no triangle' if not best else best)