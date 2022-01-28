n, h = list(map(int, input().split()))
arr = []
for _ in range(h):
    arr.append(int(input()))

if arr:
    ans = (n + 1 - arr[0]) * arr[0]
    s = (n + 1 - arr[0])
    for i in range(1, h):
        s -= (arr[i] - arr[i - 1])
        ans += (arr[i] - arr[i - 1]) * s
    print(ans)
else:
    print(0)