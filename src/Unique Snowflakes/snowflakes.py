t = int(input())

for _ in range(t):
    n = int(input())
    d = {}
    ans, j = 0, 0
    for i in range(n):
        x = int(input())
        j = max(d.get(x, 0), j)
        ans = max(ans, i - j + 1)
        d[x] = i + 1
    print(ans)