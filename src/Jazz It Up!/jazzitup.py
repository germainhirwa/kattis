from collections import Counter
LIMIT = 10**5
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
    r = []
    while n != 1:
        r.append(spf[n])
        n //= spf[n]
    return Counter(Counter(r).values())

n = int(input())-1
while True:
    pp = pf(n)
    if 1 not in pp or len(pp) > 1: n -= 1
    else: break
print(n)