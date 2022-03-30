a, b = map(int, input().split())
c, d = map(int, input().split())
m = c**2 + d**2
print((a*c + b*d)/m, (b*c-a*d)/m)