n, l = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
pos, t = 0, 0
for i in range(n):
    d, r, g = arr[i]
    inc = d - pos
    if (t + inc) % (r + g) < r:
        t = (t + inc) - (t + inc) % (r + g) + r
    else:
        t += inc
    pos = d
print(t + l - arr[-1][0])