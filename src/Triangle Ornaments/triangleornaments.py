from math import *
l = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    t1 = a*sin(acos((3*a**2 + b**2 - c**2)/(2*a*(2*a**2+2*b**2-c**2)**0.5)))
    t2 = b*sin(acos((3*b**2 + a**2 - c**2)/(2*b*(2*a**2+2*b**2-c**2)**0.5)))
    l += t1 + t2
print(l)