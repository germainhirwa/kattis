t, b = map(int, input().split())
s = list(map(int, input().split()))
v = {}
for _ in range(t):
    x, y = input().split()
    v[x] = int(y)
for i in s:
    a = 0
    for _ in range(i):
        p, n = input().split()
        a += v[p] - int(n)
    print(a)