import sys; input = sys.stdin.readline
n, k = map(int, input().split())
s, MOD = 0, 10**9+7
arr = sorted(map(int, input().split()))

def egcd(a, b):
    if a == 0: return (0, 1)
    else: y, x = egcd(b % a, a); return (x - (b // a) * y, y)

def inv_mod(a, m):
    return egcd(a, m)[0] % m

c, d = 1, 1
for i in range(k-1, n): s += arr[i]*c; c *= (i+1)*inv_mod(d, MOD); c %= MOD; s %= MOD; d += 1
print(s)