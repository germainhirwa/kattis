from math import hypot
import sys; input = sys.stdin.readline
xg, yg, xd, yd = map(float, input().split())
for x, y in [[*map(float, l.split())] for l in sys.stdin]:
    if 2*hypot(x-xg, y-yg) < hypot(x-xd, y-yd): print(f'The gopher can escape through the hole at ({x},{y}).'), exit(0)
print('The gopher cannot escape.')