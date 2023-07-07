import sys
t, w = int(input()), -1
PREC = 10**5

def success(v, s):
    for m, ck, sx, ex in s:
        D = m**2-20/v**2*ck
        if D >= 0 and sx <= (D**0.5-m)*v**2 <= ex: return 0
    return 1

for l in sys.stdin:
    if w == -1:     w, h, nb, nt = map(int, l.split()); pb, pt = [], []
    elif not pb:    pb = [*map(int, l.split())]
    elif not pt:    pt = [*map(int, l.split())]
    else:
        w = -1
        k, L, R = map(int, l.split())
        # y = k - 5/v^2 * x^2 = mx + c -> (5/v^2)x^2 + mx + (c-k) = 0
        sb, st = [], []
        for n, p, s in ((nb, pb, sb), (nt, pt, st)):
            for i in range(0, 2*n-2, 2): m = (p[i+3]-p[i+1])/(p[i+2]-p[i]); s.append((m, p[i+1]-m*p[i]-k, 10*p[i], 10*p[i+2]))
        L *= PREC; R *= PREC
        lo, hi = L, R
        while hi - lo > 1:
            mid = (lo + hi)//2
            if not success(mid/PREC, sb):   lo = mid + 1
            else:                           hi = mid
        sv = mid
        lo, hi = L, R
        while hi - lo > 1:
            mid = (lo + hi)//2
            if success(mid/PREC, st):   lo = mid
            else:                       hi = mid - 1
        res = (mid-sv)/(R-L)
        if res < 1e-5: print(0)
        else: print(res)