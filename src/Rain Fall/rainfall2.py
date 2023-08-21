l, k, t1, t2, h = map(float, input().split())
if h < l: print(h, h), exit(0)
a = t1; b = -(h+k*(t1+t2)); c = k*l; d = b*b-4*a*c
r = (-b+d**0.5)/(2*a)
if h > l: print(r*t1, r*t1)
else: print(l, r*t1)