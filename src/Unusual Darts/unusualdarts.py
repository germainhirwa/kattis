def intersect(p1, p2, p3, p4):
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
                elif i1:                    return (i1, i2)
                else:                       return None

def area(poly):
    a, n = 0, len(poly)
    for i in range(n): a += poly[i][0]*poly[(i+1)%n][1] - poly[i][1]*poly[(i+1)%n][0]
    return abs(a)/2

check = ((0, 2), (0, 3), (0, 4), (0, 5),
         (1, 3), (1, 4), (1, 5), (1, 6),
         (2, 4), (2, 5), (2, 6),
         (3, 5), (3, 6),
         (4, 6))
from itertools import permutations
for _ in range(int(input())):
    P = [[*map(float, input().split())] for _ in range(7)]
    c = float(input())
    for r in permutations(range(7)):
        p = [P[i] for i in r]
        p.append(P[0])
        ok = True
        for i, j in check:
            if intersect(p[i], p[i+1], p[j], p[j+1]): ok = False; break
        if ok:
            a = area(p)/4; a **= 3; o = r.index(0)
            if abs(a-c) < 1e-5: print(*[i+1 for i in r]); break