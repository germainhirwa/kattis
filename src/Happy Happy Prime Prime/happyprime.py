import sys
LIMIT = 10**4
spf = list(range(LIMIT+1))

p = 2
while p <= LIMIT:
    if spf[p] == p:
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
spf[1] = 0

for l in [input(), sys.stdin][1]:
    a, b = map(int, l.split())
    p = b
    while p != 1 and p != 4: p = sum(int(i)**2 for i in str(p))
    print(a, b, 'YNEOS'[(p!=1 or spf[b]!=b)::2])