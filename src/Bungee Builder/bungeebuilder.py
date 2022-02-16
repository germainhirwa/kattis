n = int(input())
arr = list(map(int, input().split()))

maxh = 0
possible = []

pos = 0
for i in range(1, n):
    if arr[i] >= arr[pos]:
        possible.append([pos, i])
        pos = i

pos = n - 1
for i in range(n - 2, -1, -1):
    if arr[i] >= arr[pos]:
        possible.append([i, pos])
        pos = i

for s, e in possible:
    for i in range(s + 1, e):
            maxh = max(maxh, min(arr[s], arr[e]) - arr[i])
print(maxh)