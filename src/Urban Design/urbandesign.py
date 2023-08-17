def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    a, b, c = y2-y1, x1-x2, (y2-y1)*x1 - (x2-x1)*y1
    d, e, f = y4-y3, x3-x4, (y4-y3)*x3 - (x4-x3)*y3
    if a == b == 0: return int((x1, y1) == (x3, y3)) if d == e == 0 else int(d*x1 + e*y1 == f and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4))
    elif d == e == 0: return int(a*x3 + b*y3 == c and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2))
    else:
        det = b*d-a*e
        if det:
            x, y = (b*f-c*e)/det, (c*d-a*f)/det
            return int(min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4))
        else:
            if a*f != c*d or b*f != c*e: return 0
            else:
                if x1 > x2 or (x1 == x2 and y1 > y2): x1, y1, x2, y2 = x2, y2, x1, y1
                if x3 > x4 or (x3 == x4 and y3 > y4): x3, y3, x4, y4 = x4, y4, x3, y3
                p, q = (x1, y1), (x2, y2)
                r, s = (x3, y3), (x4, y4)
                return int((p == r and q == s) or p <= r <= q or r <= p <= s)

import sys; input = sys.stdin.readline
MAX = 10**4; lines = []
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    dy, dx = y2-y1, x2-x1
    lines.append((x1-dx*MAX, y1-dy*MAX, x1+dx*MAX, y1+dy*MAX))
for _ in range(int(input())):
    x3, y3, x4, y4 = map(int, input().split())
    ints = 0
    for x1, y1, x2, y2 in lines: ints += intersect(x1, y1, x2, y2, x3, y3, x4, y4)
    print('different' if ints%2 else 'same')