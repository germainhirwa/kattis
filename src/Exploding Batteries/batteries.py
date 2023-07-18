import sys
from math import ceil
for l in sys.stdin:
    l = int(l)
    if l == 0: break
    print(ceil((-1+(8*l-7)**0.5)/2))