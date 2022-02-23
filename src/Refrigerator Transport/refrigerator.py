pa, ka, pb, kb, n = list(map(int, input().split()))

p = float('inf')
for a in range(n // ka + 2):
    for b in range(n // kb + 2):
        if ka * a + kb * b >= n and p >= pa * a + pb * b:
            p = pa * a + pb * b
            best = a, b
print(*best, p)