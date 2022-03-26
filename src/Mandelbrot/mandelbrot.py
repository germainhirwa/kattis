import sys

c = 1
for line in sys.stdin:
    cx, cy, r = map(float, line.split())

    x, y = 0, 0
    for _ in range(int(r)):
        x, y = x**2 - y**2 + cx, 2*x*y + cy
        if x**2 + y**2 > 4:
            break

    v = ['OUT', 'IN'][int(x**2 + y**2 < 4)]
    print(f'Case {c}: {v}')
    c += 1