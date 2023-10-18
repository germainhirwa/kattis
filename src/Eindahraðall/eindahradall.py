from math import gcd
from random import randint
MOD = 10**9+7; MOD2 = MOD**2
def miller_rabin(p):
    if p == 3: return 1
    if p % 2 == 0: return 0
    d, s = p-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for _ in range(2):
        x = pow(randint(2, p-2), d, p)
        if x == 1 or x == p-1: continue
        ok = 0
        for _ in range(s):
            x = x*x%p
            if x == 1: return 0
            if x == p-1: ok = 1; break
        if not ok: return 0
    return 1
def pollard_rho(n):
    c = 1
    while True:
        x, y, d = 2, 2, 1
        while d == 1: 
            x = (x*x+c)%n
            y = (y*y+c)%n; y = (y*y+c)%n
            d = gcd(abs(x-y), n)
        if d != n: return d
        else: c += 1
def f(n):
    if n == 1: return 1
    elif n == 2: return 500000004
    pf = {}
    if not miller_rabin(n):
        n2 = n
        while n2%2 == 0: n2 //= 2
        while n2 != 1 and not miller_rabin(n2):
            p = n2
            while not miller_rabin(p): p = pollard_rho(p)
            pf[p] = 0
            while n2%p == 0: pf[p] += 1; n2 //= p
        if n2 != 1: pf[n2] = 1
    else: pf[n] = 1
    pf = [*pf.items()]; ans = [pow(2, n, MOD2)]; fct = {1}
    def bt(idx=0, v=1, p=0, t=1):
        if idx == len(pf) or p > pf[idx][1]: return
        if v not in fct: assert n%v == 0; fct.add(v); ans[0] += t*pow(2, n//v, MOD2); ans[0] %= MOD2
        bt(idx, v*pf[idx][0], p+1, t*(pf[idx][0]-(p==0))), bt(idx+1, v, 0, t)
    bt(); ans = ans[0]*pow(2, -n, MOD2)%MOD2
    return ans//MOD*pow(n//MOD, -1, MOD)%MOD if n%MOD==0 else ans*pow(n, -1, MOD)%MOD
[print(f(int(input()))) for _ in range(int(input()))]