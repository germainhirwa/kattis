from math import *

while True:
    n = int(input())
    if n == 0:
        break
    dest = []
    for _ in range(n):
        h = input().split()
        x, y = float(h[0]), float(h[1])
        angle = float(h[3])
        for i in range(2, len(h) // 2):
            d = float(h[2*i + 1])
            if h[2*i] == 'walk':
                x += d*cos(angle*pi/180)
                y += d*sin(angle*pi/180)
            else:
                angle += d
        dest.append((x, y))
    avg = (sum(map(lambda x: x[0], dest))/len(dest), sum(map(lambda x: x[1], dest))/len(dest))
    worst = max(dest, key=lambda x: hypot(avg[0] - x[0], avg[1] - x[1]))
    print(*avg, hypot(avg[0] - worst[0], avg[1] - worst[1]))