import sys
from fractions import Fraction
for l in sys.stdin:
    f = l.strip()
    if len(f) < 6: break
    f = min([Fraction(int(f[2:i] or 0) + Fraction(int(f[i:len(f)-3]), 10**(len(f)-3-i)-1), 10**(i-2)) for i in range(2, len(f)-3)], key=lambda x: x.denominator)
    print(f'{f.numerator}/{f.denominator}')