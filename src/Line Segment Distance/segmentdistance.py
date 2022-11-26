import sys
input()
for line in sys.stdin:
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, line.split())
    # (y1-y2)x + (x2-x1)y = (y1-y2)x1 + (x2-x1)y1
    # (y3-y4)x + (x4-x3)y = (y3-y4)x3 + (x4-x3)y3
    a1, b1, c1 = y1-y2, x2-x1, (y1-y2)*x1 + (x2-x1)*y1
    a2, b2, c2 = y3-y4, x4-x3, (y3-y4)*x3 + (x4-x3)*y3
    m1, m2 = b1*a2-b2*a1, c1*a2-c2*a1 # to solve y-intersection
    #print(a1, b1, c1, a2, b2, c2, m1, m2)
    if m1 != 0 and min(y1, y2) <= m2/m1 <= max(y1, y2) and min(y3, y4) <= m2/m1 <= max(y3, y4):
        print('0.00') # intersects
    else:
        dists = float('inf')
        p1, p2, p3, p4 = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
        for (px, py), (sx, sy), (ex, ey) in ((p1, p3, p4), (p2, p3, p4), (p3, p1, p2), (p4, p1, p2)):
            # add trivial distance
            dists = min(dists, ((sx-px)*(sx-px)+(sy-py)*(sy-py))**0.5)
            dists = min(dists, ((ex-px)*(ex-px)+(ey-py)*(ey-py))**0.5)

            # vector projection in a sense
            v1 = (px-sx, py-sy)
            v2 = (ex-sx, ey-sy)
            try:
                l = (v1[0]*v2[0]+v1[1]*v2[1])/(v2[0]*v2[0]+v2[1]*v2[1])
                proj = (l*v2[0], l*v2[1])
                xp, yp = sx + proj[0], sy + proj[1]
                if min(sx, ex) <= xp <= max(sx, ex) and min(sy, ey) <= yp <= max(sy, ey):
                    dists = min(dists, ((px-xp)*(px-xp)+(py-yp)*(py-yp))**0.5) # projected point on segment
            except: pass
        print('%.2f'%(dists))

"""
Samples to try out

9
-10 0 10 0 0 -10 0 10
-10 0 10 0 -5 0 5 0
1 1 1 1 1 1 2 1
1 1 1 1 2 1 2 1
1871 5789 216 -517 189 -1518 3851 1895
252 -184 662 -100 -416 -150 186 -248
0 0 8 0 10 2 15 2
10 0 0 10 0 0 4 4
10 0 0 10 0 0 5 5
"""