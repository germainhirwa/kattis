from math import *
# https://math.stackexchange.com/questions/543496/how-to-find-the-equation-of-a-line-tangent-to-a-circle-that-passes-through-a-g
for _ in range(int(input())):
    dx, dy = map(float, input().split()); rho = 1/hypot(dx, dy)
    ad = rho**2; bd = rho*sqrt(1-rho**2)
    T1x = ad*dx - bd*dy; T1y = ad*dy + bd*dx
    T2x = ad*dx + bd*dy; T2y = ad*dy - bd*dx
    print(f'({dy-T1y},{T1x-dx},{T1x*dy-T1y*dx},{dy-T2y},{T2x-dx},{T2x*dy-T2y*dx})')