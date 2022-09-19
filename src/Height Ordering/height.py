def ins(arr):
    res = 0
    arr = arr.copy()
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                res += 1
    return res

n = int(input())
for i in range(n):
    print(i + 1, ins(list(map(int, input().split()[1:]))))