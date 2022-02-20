n = int(input())
arr = list(map(int, input().split()))
rmax, rmin = [arr[0]] * n, [arr[-1]] * n
for i in range(1, n):
    rmax[i] = max(rmax[i - 1], arr[i])
    rmin[n - i - 1] = min(rmin[n - i], arr[n - i - 1])

ans = 0
if arr[0] < rmin[1]:
    ans += 1
if arr[-1] > rmax[-2]:
    ans += 1
for i in range(1, n - 1):
    if rmax[i - 1] < arr[i] < rmin[i + 1]:
        ans += 1
print(ans)