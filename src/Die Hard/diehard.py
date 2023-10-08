from random import *
dd = [[*map(int, input().split())] for _ in range(3)]
for (i, d) in enumerate(dd):
    n = n2 = e = e2 = 0
    for u in d:
        for v in dd[(i+1)%3]:
            if u > v: n += 1
            elif u == v: e += 1
        for v in dd[(i-1)%3]:
            if u > v: n2 += 1
            elif u == v: e2 += 1
    if (n and 2*n+e >= 36) and (n2 and 2*n2+e2 >= 36): print(i+1), exit(0)
print('No dice')