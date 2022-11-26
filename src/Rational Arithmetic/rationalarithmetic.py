def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

import sys
input()
for line in sys.stdin:
    x1, y1, op, x2, y2 = line.split()
    x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
    if op == '+':
        nom, denom = x1*y2 + x2*y1, y1*y2
    elif op == '-':
        nom, denom = x1*y2 - x2*y1, y1*y2
    elif op == '*':
        nom, denom = x1*x2, y1*y2
    else:
        nom, denom = x1*y2, x2*y1
    d = gcd(abs(nom), abs(denom))
    m = nom*denom < 0
    print(f"{'-'*m}{abs(nom)//d} / {abs(denom)//d}")