def period(m):
    a, b = 1, 1
    d = {}
    for i in range(2, m**2 + 1):
        a, b = b % m, (a + b) % m
        if b not in d:
            d[b] = i
        else:
            return d[b]

n = int(input())
for _ in range(n):
    print(period(int(input())))