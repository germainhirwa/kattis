import sys
from math import log2
for y in sys.stdin:
    y = int(y)
    if y == 0: break
    f, n, b = 0, 1, 2**(y//10-194)
    while f < b:
        n += 1
        f += log2(n)
    print(n-1)