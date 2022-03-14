n, k = map(int, input().split())
if k >= n:
    print(n - 1)
else:
    print(k + int(k + (n - 1) % k != n - 1) + (n - 1) % k)