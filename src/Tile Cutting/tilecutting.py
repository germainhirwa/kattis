from math import *
LIMIT = 5*10**5
spf = list(range(LIMIT+1))
primes = [2]

p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2

def ndiv(n):
    res = 1; idx = k = 0
    while n != 1 and idx < len(primes):
        pp = primes[idx]
        if pp*pp > n: break
        if n % pp == 0:
            while n % pp == 0: n //= pp; k += 1
            if k: res *= k+1
        idx += 1; k = 0
    if n != 1: res *= 2
    return res

def fft(v, inv=False):
    n = len(v)
    if n == 1: return v
    ye, yo = fft(v[::2], inv), fft(v[1::2], inv) 
    y, a, wj = [0]*n, (2-4*inv)*pi/n, 1
    w = complex(cos(a), sin(a))
    for i in range(n//2):
        y[i] = ye[i] + wj * yo[i]
        y[i + n//2] = ye[i] - wj * yo[i]
        wj *= w
    return y

def mult(p1, p2):
    m = len(p1) + len(p2) - 1
    n = 2**(len(bin(m)) - 2)
    p1 = p1 + [0]*(n - len(p1))
    p2 = p2 + [0]*(n - len(p2))
    fft1, fft2 = fft(p1), fft(p2)
    return [round(t.real/n) for t in fft([fft1[i]*fft2[i] for i in range(n)], inv=True)][:m]

d = [0, *(ndiv(i+1) for i in range(LIMIT))]
N = mult(d, d)
for _ in range(int(input())):
    lo, hi = map(int, input().split())
    best = (0, 0)
    for i in range(lo, hi+1): best = max(best, (N[i], -i))
    print(-best[1], best[0])