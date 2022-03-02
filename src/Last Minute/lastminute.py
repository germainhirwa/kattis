a, b, c, d = list(map(int, input().split()))
print(c * d + a * int(d != 0) + b * int(c != 0) + int(c + d == 0) * min(a, b))
