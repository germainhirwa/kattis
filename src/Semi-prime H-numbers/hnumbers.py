import sys
from bisect import *
hn = set(range(5, 1_000_002, 4))
for i in range(1, 250):
    hi = 4*i+1
    for j in range(i, 50_000):
        hj = 4*j+1
        if hi*hj > 1_000_001: break
        hn.discard(hi*hj)
hn = sorted(hn); sph = set()
for i in range(len(hn)-1):
    for j in range(i, len(hn)):
        if (p:=hn[i]*hn[j]) > 1_000_001: break
        sph.add(p)
sph = sorted(sph)
for l in sys.stdin:
    l = int(l)
    if l == 0: break
    print(l, bisect_right(sph, l))