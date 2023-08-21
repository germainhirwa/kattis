import sys; input = sys.stdin.readline
a, d = map(int, input().split())
aa = [[*map(int, input().split())] for _ in range(a)]
dd = [[*map(int, input().split())] for _ in range(d)]
H = sum(x[0] for x in aa)
def f(t):
    h = tt = 0
    for dh, dt in aa:
        if tt+dt <= t: h += dh
        else: h += dh*(t-tt)/dt; break
        tt += dt
    return h
def g(t):
    h = H; tt = 0
    for dh, dt in dd:
        if tt+dt <= t: h -= dh
        else: h -= dh*(t-tt)/dt; break
        tt += dt
    return h
lo, hi = 0, max(sum(x[1] for x in aa), sum(x[1] for x in dd))
while abs(lo-hi) > 1e-7:
    mi = (lo+hi)/2
    if f(mi) < g(mi): lo = mi
    else: hi = mi
print(mi)