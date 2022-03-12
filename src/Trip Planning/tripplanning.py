import sys

n, m = map(int, input().split())

if (m, n) == (1, 2):
    print(1)
    print(1)
    sys.exit(0)
if m < n:
    print('impossible')
    sys.exit(0)

g, l = {}, {}
for line in sys.stdin:
    u, v = map(int, line.split())
    u, v = min(u, v), max(u, v)
    if v == u + 1:
        g[u] = v
        l[(u, u + 1)] = len(l) + 1
    elif (u, v) == (1, n):
        g[v] = u
        l[(n, 1)] = len(l) + 1
    else:
        l[(u, v)] = len(l) + 1

trip = []
for i in range(1, n):
    if i in g and g[i] == i + 1:
        trip.append(l[(i, i + 1)])
        continue
    print('impossible')
    sys.exit(0)
if n in g and g[n] == 1:
    for r in trip:
        print(r)
    print(l[(n, 1)])
else:
    print('impossible')