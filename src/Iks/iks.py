n = int(input())
arr = list(map(int, input().split()))

LIMIT = 10**4
sieve = [True] * (LIMIT + 1)
primes = []

p = 2
while p <= LIMIT:
    if sieve[p]:
        primes.append(p)
        for i in range(2*p, LIMIT, p):
            sieve[i] = False
    if p == 2:
        p -= 1
    p += 2

def pf(n):
    res = {}
    idx = 0
    while n != 1 and idx < len(primes):
        if n % primes[idx] == 0:
            n //= primes[idx]
            res[primes[idx]] = res.get(primes[idx], 0) + 1
        else:
            idx += 1
    if n != 1:
        is_prime = True
        for p in range(primes[idx - 1], int(n**0.5) + 2):
            if n % p == 0:
                is_prime = False
                res[p] = 1
        if is_prime: res[n] = 1
    return res

fact = [pf(i) for i in arr]
pfs = {}
for f in fact:
    for p in f:
        pfs[p] = pfs.get(p, []) + [f[p]]
m, op = 1, 0
for f in pfs:
    t = sum(pfs[f])//n
    m *= f**t
    op += sum(map(lambda x: max(0, t-x), pfs[f])) + t*(n-len(pfs[f]))
print(m, op)