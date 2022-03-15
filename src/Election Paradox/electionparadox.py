n = int(input())
arr = sorted(map(int, input().split()))
k = (n + 1) // 2
print(sum(map(lambda x: (x - 1) // 2, arr[:k])) + sum(arr[k:]))