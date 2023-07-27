from math import *

def ct(poly):
    x, a, n = 0, 0, len(poly)
    for i in range(n): x += (da:=poly[i][0]*poly[(i+1)%n][1]-poly[i][1]*poly[(i+1)%n][0])*(poly[i][0]+poly[(i+1)%n][0]); a += da
    return x/3/a, abs(a)/2

poly = [[*map(int, input().split())] for _ in range(int(input()))]
lf, rf = 1e9, -1e9
for p in poly:
    if p[1] == 0: lf = min(lf, p[0]); rf = max(rf, p[0])
xc, A = ct(poly); xp = poly[0][0]
if xp > rf:
    a = (xc-lf)*A/(lf-xp)
    b = (xc-rf)*A/(rf-xp)
    if a <= b and b >= 0: print(max(floor(a), 0), '..', ceil(b))
    else: print('unstable')
elif xp < lf:
    a = (xc-rf)*A/(rf-xp)
    b = (xc-lf)*A/(lf-xp)
    if a <= b and b >= 0: print(max(floor(a), 0), '..', ceil(b))
    else: print('unstable')
elif xp == lf:
    if xc < lf: print('unstable')
    else: print(max(floor((xc-rf)*A/(rf-xp)), 0), '..', float('inf'))
else:
    if xc > rf: print('unstable')
    else: print(max(floor((xc-lf)*A/(lf-xp)), 0), '..', float('inf'))