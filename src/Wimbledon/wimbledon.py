import sys

n = int(input())
a, b = [], []
for line in sys.stdin:
    ai, bi = map(int, line.split())
    a.append(ai)
    b.append(bi)

s, s2 = sum(a), sum(map(lambda x: x*x, a))
res = 0
for i in range(n):
    res -= b[i] * a[i] * (s - a[i])
print(res + sum(b) * (s**2 - s2) // 2)