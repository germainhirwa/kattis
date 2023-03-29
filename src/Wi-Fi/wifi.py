import sys
input()
n = m = -1
for l in sys.stdin:
    if n == m == -1:
        n, m = map(int, l.split())
        h, lo, hi = [], 0, 1e6
    elif m > 0:
        m -= 1
        h.append(int(l))
        if m == 0:
            h.sort()
            while abs(lo-hi) > 0.05:
                d = (lo+hi)/2
                p, s = 1, h[0]+d
                for i in range(1, len(h)):
                    if abs(s-h[i]) > d: p, s = p+1, h[i]+d
                if p > n: lo = d
                else: hi = d
            print(round(d, 1))
            n = m = -1