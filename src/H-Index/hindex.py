from bisect import *
s = sorted(int(input()) for _ in range(int(input())))
lo, hi = 0, len(s)
while hi-lo>1:
    mi = (hi+lo)//2
    if mi>len(s)-bisect_left(s, mi): hi = mi-1
    else: lo = mi
while hi>len(s)-bisect_left(s, hi): hi -= 1
print(hi)