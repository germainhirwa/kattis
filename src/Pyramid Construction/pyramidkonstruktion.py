h, tt, ft = map(int, input().split())
# Ideally we need 1 tt and h*(h-1) ft or 2*h*(h-1) + 1 tt
if tt == 0:
    print(1, max(0, h*(h-1) - ft))
else:
    a, b = max(0, 2 * h * (h - 1) + 1 - tt - 2 * ft), 0
    while True:
        if a > 1:
            a, b = a - 2, b + 1
            continue
        break
    print(a, b)