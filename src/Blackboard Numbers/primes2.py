import sys
from math import gcd
input()

LIMIT = 2**20 + 100
spf = list(range(LIMIT+1))
primes = []
spf[0] = spf[1] = -1
p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2

for l in sys.stdin:
    l = l.strip()
    c = p = 0
    for i in [2, 8, 10, 16]:
        try: k = int(l, i)
        except: continue
        else:
            c += 1
            can = True
            if k > LIMIT:
                for p2 in primes:
                    if k % p2 == 0:
                        can = False
                        break
                p += can
            else: p += spf[k] == k
    d = gcd(p, c)
    print(f'{p//d}/{c//d}')