x, y = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    l, u, f = list(map(float, input().split()))
    y += (u-l)*(f-1)

print(x/y)