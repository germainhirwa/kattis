from math import *
p, a, b, c, d, n = list(map(int, input().split()))

arr = [p * (sin(a * k + b) + cos(c * k + d) + 2) for k in range(1, n + 1)]

m, r = 0, arr[-1]
for i in range(n - 2, -1, -1):
    if arr[i] < r:
        r = arr[i]
    else:
        d = arr[i] - r
        m = max(m, d)
print(m)