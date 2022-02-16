import sys
n = int(input())

platforms = [[0, -1, 10001]]
for line in sys.stdin:
    y, x1, x2 = list(map(int, line.split()))
    platforms.append([y, x1, x2])
platforms.sort()

p = 0
for i in range(1, n + 1):
    for j in range(i - 1, -1, -1):
        if platforms[j][1] < platforms[i][1] + 0.5 < platforms[j][2]:
            p += platforms[i][0] - platforms[j][0]
            break
    for j in range(i - 1, -1, -1):
        if platforms[j][1] < platforms[i][2] - 0.5 < platforms[j][2]:
            p += platforms[i][0] - platforms[j][0]
            break
print(p)