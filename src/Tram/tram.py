n, s = int(input()), 0
for _ in range(n):
    x, y = map(int, input().split())
    s += y-x
print(s/n)