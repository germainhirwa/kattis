n, b = map(int, input().split())
if n == b == 2: print('1 2\n2 1'), exit(0)
if n >= b: print('impossible'), exit(0)
row, s = [*range(1, n+1)], n*(n+1)//2
LIMIT = 3000
spf = list(range(LIMIT+1))
p = 2
while p <= LIMIT:
    if spf[p] == p:
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
c = n-1
while True:
    if spf[s] == s: break
    s += 1; row[c] += 1
    if row[c] >= min(b, row[c+1]-1 if c != n-1 else 1e9): c -= 1
if spf[s] != s: print('impossible'), exit(0)
for i in range(n): print(*(row[i:]+row[:i]))