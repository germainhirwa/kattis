import sys

n = 0
for line in sys.stdin:
    if line == "0":
        sys.exit(0)
    elif n == 0:
        n = int(line)
        x, y, dx, dy = 0, 0, 0, 0
    elif sum(map(int, line.split())) == -2:
        print(f"{max(x, dx)} x {y+dy}")
        dx, dy, n = 0, 0, 0
    else:
        a, b = map(int, line.split())
        if dx + a > n:
            x = max(x, dx)
            y += dy
            dx, dy = a, b
        else:
            dx += a
            dy = max(dy, b)