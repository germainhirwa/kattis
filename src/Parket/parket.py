r, b = map(int, input().split())
for p in range(3, int((r + b)**0.5) + 2):
    if (r + b) % p == 0:
        l, w = (r + b) // p, p
        if 2*(l + w) - 4 == r:
            print(l, w)
            break