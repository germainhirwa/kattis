from math import *
h, v = map(int, input().split())
t = -h/sin(pi/180*v)
if t > 0: print(int(t))
else: print('safe')