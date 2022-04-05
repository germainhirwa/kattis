n, p = map(int, input().split())

c, k = 1, 1

# C(n, p - 1) / C(n + 1, p)
for i in range(p - 1):
    c *= (n - i) / (n + k - i)
c *= p / (n + k - p + 1)
m = c

while c >= m:
    m = max(c, m)
    c *= (k + 1) / k
    c /= (n + k + 1) / (n + k - p + 1)
    k += 1
print(m)