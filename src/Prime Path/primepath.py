LIMIT = 9999
spf = list(range(LIMIT+1))
primes = []

p = 2
while p <= LIMIT:
    if spf[p] == p:
        if p > 999: primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2

g = {i: [] for i in primes}
for i in primes:
    for j in primes:
        if sum(a!=b for a,b in zip(str(i), str(j))) == 1: g[i].append(j)

from collections import deque
for _ in range(int(input())):
    a, b = map(int, input().split())
    q, v = deque([(a, 0)]), {a}
    while q:
        u, d = q.popleft()
        if u == b: print(d); break
        for i in g[u]:
            if i not in v: v.add(i), q.append((i, d+1))