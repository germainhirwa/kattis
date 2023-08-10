import sys
from math import *
def v(p, lo, hi):
    ans = 0
    for i in range(len(p)): ans += p[i]/(i+1)*(hi**(i+1)-lo**(i+1))
    return ans*pi
tc = 1; t = 0
for l in sys.stdin:
    if t == 0: d = int(l); t += 1
    elif t == 1: p = [*map(float, l.split())]; t += 1
    else:
        p2 = [0]*(2*len(p)-1)
        for i in range(len(p)):
            for j in range(len(p)): p2[i+j] += p[i]*p[j]
        lo, hi, inc = map(float, l.split())
        vb = v(p2, lo, hi)
        print(f'Case {tc}:', '%.2f'%vb)
        if vb < inc: print('insufficient volume')
        else:
            s = [lo]
            while s[-1] <= hi:
                ll, hh = s[-1], 1e9
                while abs(ll-hh) > 1e-6:
                    m = (ll+hh)/2
                    if v(p2, s[-1], m) < inc: ll = m
                    else: hh = m
                s.append(m)
            print(*map(lambda x: '%.2f'%(x-lo), s[1:-1][:8]))
        tc += 1; t = 0