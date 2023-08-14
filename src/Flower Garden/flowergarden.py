import sys; input = sys.stdin.readline
from math import *

LIMIT = 20001
spf = list(range(LIMIT+1))
primes = {0, 2}
p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.add(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2

for _ in range(int(input())):
    n, d = map(int, input().split())
    p = [[*map(int, input().split())] for _ in range(n)]
    D = [0]; px = py = 0
    for x, y in p:
        D.append(D[-1]+hypot(px-x, py-y)); px, py = x, y
        if D[-1] > d: D.pop(); break
    for i in range(len(D)-1, -1, -1):
        if i in primes: print(i); break