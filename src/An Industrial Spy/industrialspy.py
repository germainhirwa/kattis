LIMIT = 10**7
spf = list(range(LIMIT+1))
spf[0] = spf[1] = -1
p = 2
while p <= LIMIT:
    if spf[p] == p:
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
from itertools import permutations
for _ in range(int(input())):
    ans = set()
    seen = set()
    for p in permutations(map(int, input().strip())):
        if p in seen: continue
        seen.add(p)
        for i in range(1, 1<<len(p)):
            d = 0
            for j in range(len(p)):
                if i&(1<<j): d *= 10; d += p[j]
            if spf[d] == d: ans.add(d)
    print(len(ans))