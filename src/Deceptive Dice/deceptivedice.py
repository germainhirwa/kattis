from math import ceil
n, k = map(int, input().split())
e = (n+1)/2
for _ in range(k-1):
    lb = ceil(e)-1
    e = (lb*e + (n+lb+1)*(n-lb)/2)/n
print(e)