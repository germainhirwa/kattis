from math import *
n, g = map(float, input().split()); n = int(n)
vv = [0]
for _ in range(n):
    d, a = map(int, input().split())
    vv = [*(sqrt(v*v+2*g*d*cos(a*pi/180)) for v in vv), 0]
for i in vv[:-1]: print(i)