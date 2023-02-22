LIMIT = 13*10**5
spf = list(range(LIMIT+1))
primes, primes2 = [], []

p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(str(p))
        primes2.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
a = 0
l, h = map(int, input().split())
pref = input().strip()
for i in range(l-1, h): a += primes[i].find(pref) != -1
print(a)