from math import *
d, s = map(int, input().split())
# f(x) = s+x(1-cosh(d/2x)) is increasing :)
prec = 10**17
lo, hi = 0, prec*10**9
while abs(lo-hi) > 1:
    mi = (lo+hi)//2
    if s*prec+mi*(1-cosh(0.5*d*prec/mi)) < 0: lo = mi
    else: hi = mi
print(2*mi*sinh(0.5*d*prec/mi)/prec)