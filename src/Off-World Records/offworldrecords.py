n, c, p = map(int, input().split()); s = 0
for h in (int(input()) for _ in range(n)):
    if h > c+p: c, p = p, h; s += 1
print(s)