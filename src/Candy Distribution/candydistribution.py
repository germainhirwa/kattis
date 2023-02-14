def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def inv_mod(a, m):
    g, x, y = egcd(a, m)
    if g != 1: raise Exception
    else: return x % m

import sys
input()
for line in sys.stdin:
    k, c = map(int, line.split())
    try:
        if k == 1:
            if c == 1: print(2)
            else: print(1)
        elif c == 1:
            print(k+1)
        else:
            i = inv_mod(c, k)
            if i > 10**9 or i < 1: raise Exception
            print(i)
    except: print('IMPOSSIBLE')