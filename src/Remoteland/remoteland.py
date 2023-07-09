import sys

LIMIT = 5*10**6
spf = list(range(LIMIT+1))
primes = [2]
p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2

def powmod(a, b, m):
    if b == 0: return 1
    elif b == 1: return a
    elif b % 2: return a * powmod(a * a % m, b // 2, m) % m
    return powmod(a * a % m, b // 2, m)

MOD = 10**9+7
for l in map(int, sys.stdin):
    if l == 0: break
    m = 1
    for p in primes:
        if p > l//2: break
        s, l2 = 0, l//p
        while l2: s += l2; l2 //= p
        m = (m*powmod(p, s-s%2, MOD))%MOD
    print(m)