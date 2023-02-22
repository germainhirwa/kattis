import sys

LIMIT = int(10**4.5)
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

def pf(n):
    res = idx = 0
    while n != 1 and idx < len(primes):
        if n % primes[idx] == 0:
            n //= primes[idx]
            res += primes[idx]
        else:
            idx += 1
    if n != 1:
        is_prime = True
        for p in range(primes[idx - 1], int(n**0.5) + 2):
            if n % p == 0:
                is_prime = False
                res += p
        if is_prime: res += n
    return res

def red(n):
    it = 0
    while True:
        it += 1
        r = pf(n)
        if n == r: break
        n = r
    return (n, it)

for i in sys.stdin:
    if int(i) == 4: break
    print(*red(int(i)))