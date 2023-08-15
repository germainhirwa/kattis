import sys; input = sys.stdin.readline
from collections import Counter
f = [1]; MOD = 10**9+7
for i in range(10**5): f.append((f[-1]*(i+1))%MOD)
for _ in range(int(input())):
    n = int(input()); l = [*map(int, input().split())]; m = int(input()); c = Counter(); w = [input().strip() for _ in range(m)]
    for p in w: c[(p[0], len(p))] += 1
    h = [p for p in w if len(p) == n]; ans = 0
    for s in h:
        k = Counter(); d = 1
        for i in range(n): k[(s[i], l[i])] += 1
        c[(s[0], n)] -= 1
        for q in k:
            r, t = c[q], k[q]
            if c[q] < k[q]: d = 0; break
            d *= f[c[q]]*pow(f[c[q]-k[q]], -1, MOD); d %= MOD
        c[(s[0], n)] += 1
        ans += d; ans %= MOD
    print(ans)