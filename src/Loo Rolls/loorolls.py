l,n = list(map(int,input().split()))
k = 1
while l % n:
    k += 1
    n -= l % n
print(k)