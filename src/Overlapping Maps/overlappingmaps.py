import sys
from math import *
for l in sys.stdin:
    w, h, x, y, s, r = map(int, l.split())
    if w == h == 0: break
    s /= 100; r *= pi/180
    # (cos-s)a+sin*b=x, -sin*a+(cos-s)*b=y
    a, b, e, c, d, f = cos(r)-s, sin(r), x, -sin(r), cos(r)-s, y
    A = (e*d-b*f)/(a*d-b*c); B = (a*f-c*e)/(a*d-b*c)
    print('%.2f %.2f'%(cos(r)*A+sin(r)*B, cos(r)*B-sin(r)*A))