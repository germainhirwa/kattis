import sys

LIMIT = 1 << 15
sieve = [True] * LIMIT
primes = []

p = 2
while p < LIMIT:
    if sieve[p]:
        primes.append(p)
        for i in range(2*p, LIMIT, p):
            sieve[i] = False
    if p == 2:
        p -= 1
    p += 2

for line in sys.stdin:
    k = int(line)
    if k == 0:
        break

    dup = k
    for p in primes:
        if k % p == 0:
            k //= p
            k *= (p - 1)
            while dup % p == 0:
                dup //= p
    if dup == 1:
        print(k)
    else:
        print(k * (dup - 1) // dup)