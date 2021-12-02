r, c = list(map(int, input().split()))
m = []
p = 0

def neighbours(rn, cn):
    res = []
    if rn >= 1:
        if cn >= 1:
            res.append([rn - 1, cn - 1])
        if cn < c - 1:
            res.append([rn - 1, cn + 1])
        res.append([rn - 1, cn])
    if rn < r - 1:
        if cn >= 1:
            res.append([rn + 1, cn - 1])
        if cn < c - 1:
            res.append([rn + 1, cn + 1])
        res.append([rn + 1, cn])
    if cn >= 1:
        res.append([rn, cn - 1])
    if cn < c - 1:
        res.append([rn, cn + 1])
    return res

import sys
for line in sys.stdin:
    tmp = list(line.strip())
    for i in tmp:
        if i == "o":
            p += 1
    m.append(tmp)

n = []
for _ in range(r):
    n.append([0] * c)
for i in range(r):
    for j in range(c):
        for rk, ck in neighbours(i, j):
            if m[rk][ck] == "o":
                n[i][j] += 1

if p != r * c:
    mi, mj, mp = 0, 0, 0
    for i in range(r):
        for j in range(c):
            if m[i][j] == "." and n[i][j] > mp:
                mi, mj, mp = i, j, n[i][j]

    for rk, ck in neighbours(mi, mj):
        n[rk][ck] += 1

    m[mi][mj] = "o"

ans = 0
for i in range(r):
    for j in range(c):
        if m[i][j] == "o":
            ans += n[i][j]

print(ans // 2)