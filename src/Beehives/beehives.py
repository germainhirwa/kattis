from math import hypot
while True:
    d, n = map(float, input().split())
    if d + n == 0: break
    n = int(n)
    f, h = [0]*n, []
    for i in range(n):
        x, y = map(float, input().split())
        h.append((x, y, i))
    for x1, y1, i1 in h:
        for x2, y2, i2 in h:
            if i1 == i2: continue
            if hypot(x1-x2, y1-y2) <= d: f[i1] = f[i2] = 1
    print(f'{sum(f)} sour, {n-sum(f)} sweet')