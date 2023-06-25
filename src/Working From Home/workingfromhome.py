from math import ceil
m, p, n = map(int, input().split())
w = [int(input()) for _ in range(n)]
base, target, eps = m, m, 0
for i in range(n):
    offset = w[i] - target
    eps += offset >= 0
    target = base - ceil(offset*p/100)
print(eps)