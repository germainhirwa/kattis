from random import *
import sys

LIMIT = 10**4
spf = list(range(LIMIT+1))
primes = []
p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2

def check(p): # Miller-Rabin
    if p == 2: return 0
    if p == 3: return 1
    d, s = p-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for _ in range(3):
        x = pow(randint(2, p-2), d, p)
        for _ in range(s):
            y = x**2 % p
            if y == 1 and x != 1 and x != p-1: return 0
            x = y
        if y != 1: return 0
    return 1

input()
for l in sys.stdin:
    i = int(l)
    if i % 2: print(2 if check(i+2) else -1)
    else:
        pp = 0
        for p in primes:
            if check(p+i): pp = p; break
        print(pp if pp else -1)