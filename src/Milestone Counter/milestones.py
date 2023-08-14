import sys; input = sys.stdin.readline
from fractions import Fraction
m, n = map(int, input().split())
t = [*map(int, input().split())]
x = [*map(int, input().split())]
can = set()
for i in range(n-m+1):
    ok = True
    f = Fraction(x[i+1]-x[i], t[1]-t[0])
    for j in range(m-1):
        if (t[j+1]-t[j])*f != x[i+j+1]-x[i+j]: ok = False
    if ok: can.add(x[i+1]-x[i])
print(len(can)), print(*sorted(can))