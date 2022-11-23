t, s, n = map(int, input().split())
u, d = s, 0
a = list(map(int, input().split())) + [t]
c = a[0]
for i in range(1, n + 1):
    d, u, c = max(0, u - a[i] + c), min(s, d + a[i] - c), a[i]
print(d)