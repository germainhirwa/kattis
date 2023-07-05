from math import ceil
x, lo, hi = map(int, input().split())
it, mi, ma = 0, 1e9, -1
while True:
    if lo <= ceil(x) <= hi: mi, ma = min(mi, it), max(ma, it)
    x = 10*(x**0.5); it += 1
    if x == 100: break
if hi == 100: ma = float('inf')
if mi == 1e9: print('impossible')
else: print(mi, ma)