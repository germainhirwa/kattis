n, m = map(int, input().split())
LIMIT = int(n**0.5) + 10
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

res = {}
idx = 0
while n != 1 and idx < len(primes):
    if n % primes[idx] == 0:
        n //= primes[idx]
        if primes[idx] not in res: res[primes[idx]] = 0
        res[primes[idx]] += 1
    else:
        idx += 1
if n != 1:
    is_prime = True
    for p in range(primes[idx - 1], LIMIT-8):
        if n % p == 0:
            is_prime = False
            res[p] = 1
    if is_prime: res[n] = 1

k = float('inf')
for p, v in res.items():
    n2, v2 = m, 0
    while n2: n2 //= p; v2 += n2
    k = min(k, v2//v)
print(k)