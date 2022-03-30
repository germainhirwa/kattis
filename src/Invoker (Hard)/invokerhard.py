a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())
m = e**2 + f**2 + g**2 + h**2
print(
    (c*g + d*h + a*e + b*f)/m,
    (d*g - c*h - a*f + b*e)/m,
    (b*h - d*f - a*g + c*e)/m,
    (c*f - b*g - a*h + d*e)/m
)