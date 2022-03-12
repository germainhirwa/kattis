from math import *
m, n, r = map(float, input().split())
ax, ay, bx, by = map(int, input().split())
print(abs(ay - by) * r / n + min(2, abs(pi * (ax - bx) / m)) * min(ay, by) / n * r)