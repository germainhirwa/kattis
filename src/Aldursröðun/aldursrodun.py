from itertools import *; from math import *
n = int(input()); c = [*map(int, input().split())]
for p in permutations(c):
    ok = 1
    for i in range(n-1):
        if gcd(p[i], p[i+1]) == 1: ok = 0; break
    if ok: print(*p); exit(0)
print('Neibb')