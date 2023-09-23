from math import *
k, w, l = map(int, input().split())
def f(a):
    s = w/2*tan(a)
    for _ in range(k-1): a = atan(2*tan(a)); s += w*tan(a)
    return s + w*tan(a)
lo, hi = 0, pi/2
while abs(lo-hi)>1e-8:
    mi = (lo+hi)/2
    if f(mi) > l: hi = mi
    else: lo = mi
print(mi*180/pi)