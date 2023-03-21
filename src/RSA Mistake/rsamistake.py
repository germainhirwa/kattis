LIMIT = 10**6
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
    
a, b = map(int, input().split())
pa, pb = pf(a), pf(b)
if a != b and a in pa and b in pb:
    print('full credit')
else:
    pc = pa.copy()
    for k, v in pb.items():
        if k in pc: pc[k] += v
        else: pc[k] = v
    print('partial credit' if max(pc.values()) < 2 else 'no credit')