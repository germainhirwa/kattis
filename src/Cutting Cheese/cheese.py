from math import *
n, s = map(int, input().split())
ss = [[*map(lambda x: float(x)/1000, input().split())] for _ in range(n)]
def v(lo, hi):
    ans = (hi-lo)*10000
    for r, _, _, z in ss:
        ll, hh = min(max(z-r, lo), hi), max(min(z+r, hi), lo)
        if ll == hh: continue
        ll -= z; hh -= z; ll /= r; hh /= r
        ans -= pi*((hh-ll)-hh**3/3+ll**3/3)*r**3
    return ans
target = v(0, 100)/s
res = [0]
while len(res) != s:
    lo, hi = res[-1], 100
    while abs(lo-hi)>1e-7:
        m = (lo+hi)/2
        if v(res[-1], m) < target: lo = m
        else: hi = m
    res.append(m)
res.append(100)
for i in range(s): print(res[i+1]-res[i])