n, m = map(int, input().split())
# find all (a, b) such that a*b == m and max(a,b) <= n
p, a = 1, 0
while p*p <= m and p <= n:
    if m % p == 0 and m // p <= n:
        if p*p == m: a += 1
        else: a += 2
    p += 1
print(a)