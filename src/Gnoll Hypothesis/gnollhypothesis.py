from math import *
n, k = map(int, input().split())
s = [*map(float, input().split())]
p = [comb(n-1, n-k)]
for t in range(n-k): p.append(p[-1]*(n-k-t)//(n-1-t))
pp = [0]*n
for i in range(n):
    for j in range(len(p)): pp[(i+j)%n] += p[j]*s[i]
ss = sum(pp)/100
for i in range(n): pp[i] /= ss
print(*pp)