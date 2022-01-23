n, cap = list(map(int, input().split()))
pos, neg = [], []
import sys
for line in sys.stdin:
    a, b = list(map(int, line.split()))
    if a <= 0:
        neg.append([-a, b])
    else:
        pos.append([a, b])
pos.sort()
neg.sort()

dist = 0
for a in [neg, pos]:
    for i in range(len(a)):
        while a[i][1] >= cap:
            a[i][1] -= cap
            dist += 2 * a[i][0]
    a.reverse()
    for i in range(len(a)):
        tmp, j, cp, d = cap, i, 0, 0
        while tmp > 0 and j < len(a):
            if a[j][1] != 0:
                d = max(d, a[j][0])
            tmp, a[j][1] = max(0, tmp - a[j][1]), max(0, a[j][1] - tmp)
            j += 1
        dist += 2 * d
print(dist)