from math import gcd
a, b = map(int, input().split('/'))
c, d = 5*a-160*b, 9*b
e = gcd(c, d)
print(f'{c//e}/{d//e}')