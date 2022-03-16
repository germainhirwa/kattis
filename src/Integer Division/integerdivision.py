n, d = map(int, input().split())
dd = {}
a = list(map(lambda x: int(x) // d, input().split()))
for k in a:
    if k not in dd:
        dd[k] = 0
    dd[k] += 1
print(sum(map(lambda x: x * (x - 1) // 2, dd.values())))