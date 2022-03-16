def spd(n):
    s, p = 0, 1
    while p * p <= n:
        if n % p == 0:
            s += p
            if p * p != n:
                s += n // p
        p += 1
    return s - n

import sys

for line in sys.stdin:
    n = int(line)
    s = spd(n)
    if s == n:
        print(n, 'perfect')
    elif abs(s - n) <= 2:
        print(n, 'almost perfect')
    else:
        print(n, 'not perfect')