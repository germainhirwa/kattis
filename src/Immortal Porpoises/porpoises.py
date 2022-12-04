pisano_period = 1500000000
MOD = 10**9
input()

mem = {}
def f(n):
    if n in mem: return mem[n]
    if n < 2: return n
    if n % 2:
        res = (f((n + 1) // 2)**2 + f(n // 2)**2) % MOD
    else:
        fh, fhm = f(n // 2), f(n // 2 - 1)
        res = (fh * (fh + 2 * fhm)) % MOD
    mem[n] = res
    return res

import sys
sys.setrecursionlimit(10**5)
for line in sys.stdin:
    t, n = map(int, line.split())
    print(t, f(n % pisano_period))