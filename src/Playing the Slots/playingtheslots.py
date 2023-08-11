from math import *
p = [[*map(float, input().split())] for _ in range(int(input()))]
best = 1e9
for i in range(len(p)):
    x1, y1 = p[i]
    x2, y2 = p[(i+1)%len(p)]
    dx = x2-x1; dy = y2-y1
    a = pi/2-atan2(dy, dx)
    r = [x*cos(a)-y*sin(a) for x, y in p]
    best = min(best, max(r)-min(r))
print(best)