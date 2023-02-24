from math import *
d, x, y, h = map(int, input().split())
a, b, c = atan2(y+h/2,x), atan2(y,x), atan2(y-h/2,x)
print(d*(tan(a-b) + tan(b-c)))