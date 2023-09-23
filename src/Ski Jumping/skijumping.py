import sys; input = sys.stdin.readline
from math import *
g = 9.81

def h(l):
    if l < 0: return H
    elif l < L/2: return H*(1-2*(l/L)**2)
    elif l < L: return 2*H*(l/L-1)**2
    return 0

def dh(l):
    if 0 < l < L/2: return -4*H*l/L/L
    elif L/2 <= l < L: return 4*H*(l/L-1)/L
    return 0

def f(l):
    return -g/2*(l/v0)**2 + H + p

for _ in range(int(input())):
    j, p, H, L = map(int, input().split())
    v0 = (2*g*j)**0.5
    lo, hi = 0, 1e5
    while abs(lo-hi)>1e-6:
        mi = (lo+hi)/2
        if f(mi)-h(mi) > 0: lo = mi
        else: hi = mi
    v = (2*g*(p+H-f(mi)))**0.5
    va = (v0, -v)
    vb = (1, dh(mi))
    a = acos((va[0]*vb[0]+va[1]*vb[1])/(hypot(*va)*hypot(*vb)))
    print(mi, hypot(v, v0), a*180/pi)