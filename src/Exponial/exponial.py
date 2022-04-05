import sys
sys.setrecursionlimit(10**4)

n, m = map(int, input().split())
def f(n):
    if n == 1:
        return 1
    return n ** f(n - 1)

def totient(n):
    ans = n
    temp = n
    p = 2
    while p * p <= n:
        if temp % p == 0:
            ans *= (p - 1)
            ans //= p
            while temp % p == 0:
                temp //= p
        p += 1
    return ans if temp == 1 else ans // temp * (temp - 1)

def expmod(a, b, m):
    if b == 0:
        return 1
    elif b % 2:
        return a * expmod(a, b - 1, m) % m
    return expmod(a * a % m, b // 2, m)

# f(n) % m
def expomod(n, m):
    if m == 1:
        return 0
    if n <= 4:
        return f(n) % m
    else:
        p = totient(m)
        return expmod(n, p + expomod(n - 1, p), m)

print(expomod(n, m))