def prime(n):
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        if p == 2:
            p -= 1
        p += 2
    return True

def fep(b, e, p):
    if e == 0:
        return 1
    elif e % 2:
        return (b * fep(b, e - 1, p)) % p
    k = fep(b, e // 2, p)
    return k**2 % p

import sys

for line in sys.stdin:
    p, a = map(int, line.split())
    if p == 0:
        break
    if prime(p):
        print('no')
    else:
        print(['no', 'yes'][int(fep(a, p, p) == a)])