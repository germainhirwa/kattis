import sys
from math import ceil

n, k = map(int, input().split())
t = list(map(int, sys.stdin))
t = list(map(lambda x: (x, 1), t))
t2 = sorted(t + list(map(lambda x: (x[0]+1000, -1), t)))
m = c = 0
for tt, i in t2:
    c += i
    m = max(m, c)
print(ceil(m/k))