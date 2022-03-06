n = int(input())
arr = [1, 2, 4]
if n <= 3:
    print(arr[n - 1])
else:
    for i in range(n - 3):
        arr.append(arr[-1] + arr[-2] + arr[-3])
    print(arr[-1])