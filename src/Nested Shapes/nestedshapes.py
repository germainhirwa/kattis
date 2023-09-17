from math import *
n, c = input().split(); n = int(n)
x, m = input().split(); m = int(m)
if x == 'A': r = [m, m/pi][c[0] < 'D']**0.5
else: r = [m/4, m/pi/2][c[0] < 'D']
w = input()
for i in range(n-1):
    if c[i] < 'D': r *= 2**0.5
    elif c[i+1] < 'D': r /= 2
    else: r /= 2**0.5
if w == 'A': print(r*r*[1, pi][c[-1] < 'D'])
else: print(2*r*[2, pi][c[-1] < 'D'])