from math import *
for _ in range(int(input())):
    t, n, m = map(int, input().split())
    r = [1/(1/sin(pi/n)-1)]
    for _ in range(m-1):
        rr = r[-1]
        lo, hi = rr, 1e10
        while abs(lo-hi)>1e-7:
            mi = (lo+hi)/2
            if acos(mi/(rr+mi))+asin(rr/(rr+mi)) > pi*(n-2)/2/n: lo = mi
            else: hi = mi
        r.append(mi)
    R = r[-1]
    print(t, '%.3f'%R, '%.3f'%(2*R*(pi+n)))