l, w, n, r = map(int, input().split())
c = [[*map(int, input().split())] for _ in range(n)]
p = [(-l/2, 0), (l/2, 0), (0, -w/2), (0, w/2)]
for x, y in c:
    if all((x-xp)**2 + (y-yp)**2 <= r**2 for xp, yp in p): print(1), exit(0)
for i in range(n-1):
    x1, y1 = c[i]
    for j in range(i+1, n):
        x2, y2 = c[j]
        if all(any((x-xp)**2 + (y-yp)**2 <= r**2 for x, y in ((x1, y1), (x2, y2))) for xp, yp in p): print(2), exit(0)
for i in range(n-2):
    x1, y1 = c[i]
    for j in range(i+1, n-1):
        x2, y2 = c[j]
        for k in range(j+1, n):
            x3, y3 = c[k]
            if all(any((x-xp)**2 + (y-yp)**2 <= r**2 for x, y in ((x1, y1), (x2, y2), (x3, y3))) for xp, yp in p): print(3), exit(0)
for i in range(n-3):
    x1, y1 = c[i]
    for j in range(i+1, n-2):
        x2, y2 = c[j]
        for k in range(j+1, n-1):
            x3, y3 = c[k]
            for m in range(k+1, n):
                x4, y4 = c[m]
                if all(any((x-xp)**2 + (y-yp)**2 <= r**2 for x, y in ((x1, y1), (x2, y2), (x3, y3), (x4, y4))) for xp, yp in p): print(4), exit(0)
print('Impossible')