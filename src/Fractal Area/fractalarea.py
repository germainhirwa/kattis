import sys
from math import pi
input()
for l in sys.stdin:
    r, n = map(int, l.split())
    print(sum((1-0.25*(i>1))**(i-1)*pi*r**2 for i in range(n)))