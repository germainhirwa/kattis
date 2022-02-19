h, w, n, m = list(map(int, input().split()))
mat, ker, res = [], [], [[0 for _ in range(w - m + 1)] for _ in range(h - n + 1)]
for _ in range(h):
    mat.append(list(map(int, input().split())))
for _ in range(n):
    ker.append(list(map(int, input().split()))[::-1])
ker.reverse()

for i in range(n):
    for j in range(m):
        t = ker[i][j]
        for k in range(h - n + 1):
            for l in range(w - m + 1):
                res[k][l] += t * mat[k + i][l + j]
for r in res:
    print(*r)