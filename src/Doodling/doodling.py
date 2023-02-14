from math import gcd
import sys
input()

def doodle(x, y):
    x, y = x-1, y-1
    d = gcd(x, y)
    return x*y//d + 1 - (x//d-1)*(y//d-1)//2

for line in sys.stdin:
    x, y = map(int, line.split())
    print(doodle(x, y))