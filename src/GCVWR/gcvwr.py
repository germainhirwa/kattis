g, t, n = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(9 * (g - t) // 10 - sum(arr))