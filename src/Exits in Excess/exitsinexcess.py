import sys

v, e = map(int, input().split())
l, r = [], []
el = {}
for _ in range(v + 1):
    l.append([])
    r.append([])

for line in sys.stdin:
    s, d = map(int, line.split())
    [l, r][int(s < d)][s].append(d)
    el[(s, d)] = len(el) + 1

k = sum(map(len, l))
if k <= e // 2:
    print(k)
    for i in range(1, v + 1):
        for j in l[i]:
            print(el[(i, j)])
else:
    print(e - k)
    for i in range(1, v + 1):
        for j in r[i]:
            print(el[(i, j)])