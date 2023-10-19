import sys

n, b = list(map(int, input().split()))
if b in [1, n]:
    print(1)
    sys.exit(0)

arr = list(map(int, input().split()))
d = {}

for i in range(n):
    d[arr[i]] = i
idx = d[b]

left, right = {}, {}

gt, lt = 0, 0
for j in range(idx, -1, -1):
    if arr[j] > b:
        gt += 1
    elif arr[j] < b:
        lt += 1
    if gt - lt in left:
        left[gt - lt] += 1
    else:
        left[gt - lt] = 1

gt, lt = 0, 0
for j in range(idx, n):
    if arr[j] > b:
        gt += 1
    elif arr[j] < b:
        lt += 1
    if gt - lt in right:
        right[gt - lt] += 1
    else:
        right[gt - lt] = 1

ans = 0
for i in range(-n, n):
    if i in left and -i in right:
        ans += left[i] * right[-i]
print(ans)