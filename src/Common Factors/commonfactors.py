from math import gcd
n = int(input())

LIMIT = 10**3
spf = list(range(LIMIT+1))
primes = []
p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2

a, b = 1, 1
for p in primes:
    if b*p <= n: a, b = a*(p-1), b*p
    else: break
d = gcd(b-a, b)
print(f'{(b-a)//d}/{b//d}')