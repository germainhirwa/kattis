a, b = map(int, input().split())
d = {}
p = 2
if a % b != 0:
    print(0)
else:
    n = a // b
    l = n
    while n != 1 and p <= l:
        while n % p == 0:
            d[p] = d.get(p, 0) + 1
            n //= p
        p += 1
    r = 1
    for i in d.values():
        r *= i + 1
    print(r)