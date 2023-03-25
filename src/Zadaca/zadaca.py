from math import log10

LIMIT = int(10**4.5+10)
spf = list(range(LIMIT+1))
primes = []

# If p is prime, spf[p] == p
p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2

# Prime factorization
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

n, a, m, b = int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))
pfa, pfb = {}, {}
for i in a:
    for k, v in pf(i).items():
        if k not in pfa: pfa[k] = 0
        pfa[k] += v
for i in b:
    for k, v in pf(i).items():
        if k not in pfb: pfb[k] = 0
        pfb[k] += v
pfc = {}
for i in pfa:
    if i in pfb: pfc[i] = min(pfa[i], pfb[i])
r, l = 1, 0
MOD = 10**9
for k, v in pfc.items():
    r = r*pow(k, v, MOD) % MOD
    l += v*log10(k)
print(str(r).zfill(min(9, int(l))))