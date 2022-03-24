import sys
from collections import deque

n = int(input())
xs, ys, xt, yt = map(int, input().split())

# If using early goal test, include this
if (xs, ys) == (xt, yt):
    print(0)
    sys.exit(0)

sx, sy = {}, {}
for line in sys.stdin:
    x, y = map(int, line.split())
    if x not in sy:
        sy[x] = []
    sy[x].append(y)
    if y not in sx:
        sx[y] = []
    sx[y].append(x)

TWOMIL = 2 * 10**9
for s in (sx, sy):
    temp = {}
    for k in s:
        s[k].sort()
        d = {}
        for i in range(len(s[k])):
            d[s[k][i]] = i
        temp[k + TWOMIL] = d
    s.update(temp)

q = deque([(xs, ys, 0)])
vis = {(xs, ys)}
while q:
    xu, yu, d = q.popleft()
    for dx, dy in ((2, 1), (2, -1), (-2, 1), (-2, -1)):
        if 0 <= sx[yu + TWOMIL][xu] + dx < len(sx[yu]):
            xn = sx[yu][sx[yu + TWOMIL][xu] + dx]
            if 0 <= sy[xn + TWOMIL][yu] + dy < len(sy[xn]):
                yn = sy[xn][sy[xn + TWOMIL][yu] + dy]
                if (xn, yn) not in vis:
                    if (xn, yn) == (xt, yt):
                        print(d + 1)
                        sys.exit(0)
                    vis.add((xn, yn))
                    q.append((xn, yn, d + 1))
    for dx, dy in ((1, 2), (1, -2), (-1, 2), (-1, -2)):
        if 0 <= sy[xu + TWOMIL][yu] + dy < len(sy[xu]):
            yn = sy[xu][sy[xu + TWOMIL][yu] + dy]
            if 0 <= sx[yn + TWOMIL][xu] + dx < len(sx[yn]):
                xn = sx[yn][sx[yn + TWOMIL][xu] + dx]
                if (xn, yn) not in vis:
                    if (xn, yn) == (xt, yt):
                        print(d + 1)
                        sys.exit(0)
                    vis.add((xn, yn))
                    q.append((xn, yn, d + 1))
print(-1)