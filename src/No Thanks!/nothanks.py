n = int(input()) + 1
arr = [-1] + sorted(map(int, input().split()))
print(sum(map(lambda i: arr[i], filter(lambda i: arr[i] != arr[i - 1] + 1, range(1, n)))))