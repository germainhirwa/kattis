import sys; input = sys.stdin.readline
for _ in range(int(input())):
    s = 0
    for _ in range(int(input())):
        x, y = map(int, input().split())
        for p in range(1, 12):
            if x**2+y**2 <= 400*p**2: break
        s += 11-p
    print(s)