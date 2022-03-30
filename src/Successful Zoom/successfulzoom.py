n = int(input())
arr = tuple(map(int, input().split()))
k, found = 1, False
while k <= n // 2 and not found:
    m = arr[k - 1] - 1
    found = True
    for i in range(k - 1, n, k):
        if arr[i] <= m:
            found = False
            break
        m = arr[i]
    k += 1
print(k - 1 if found else 'ABORT!')