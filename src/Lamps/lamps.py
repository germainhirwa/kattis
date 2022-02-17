h, p = list(map(int, input().split()))
a = 0

ib, lel = 0, 0
while ib <= lel:
    a += 1
    ib, lel = (a * h + 999) // 1000 * 5 + (60 * a * h * p) / 10**5, (a * h + 7999) // 8000 * 60 + (11 * a * h * p) / 10**5
print(a)