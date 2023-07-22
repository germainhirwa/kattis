r, c = map(int, input().split())
m = [[*map(int, input().split())] for _ in range(r)]
d1, d2 = {}, {}
for i in range(r):
    for j in range(c):
        if m[i][j] != -1: d1[m[i][j]] = r-1-i-j; d2[m[i][j]] = r-1-i+j
m1, m2 = {}, {}
s = sorted(m[i][j] for i in range(r) for j in range(c) if m[i][j] != -1)
ans = 1e9
for _ in range(2):
    sr1, sr2, sc1, sc2 = 0, r-1, 0, 0
    pr1, pr2, pc1, pc2 = sr1, sr2, sc1, sc2
    dr1, dr2, dc1, dc2 = 1, 0, 0, 1
    for i in s:
        while True:
            works = 0
            if m[pr1][pc1] != -1: works, m1[i] = 1, r-1-pr1-pc1
            pr1 -= 1; pc1 += 1
            if not (0<=pr1<r and 0<=pc1<c):
                sr1 += dr1; sc1 += dc1
                if not (0<=sr1<r and 0<=sc1<c):
                    sr1 -= dr1; sc1 -= dc1
                    dr1, dc1 = -dc1, dr1
                    sr1 += dr1; sc1 += dc1
                pr1, pc1 = sr1, sc1
            if works: break
        while True:
            works = 0
            if m[pr2][pc2] != -1: works, m2[i] = 1, r-1-pr2+pc2
            pr2 -= 1; pc2 -= 1
            if not (0<=pr2<r and 0<=pc2<c):
                sr2 += dr2; sc2 += dc2
                if not (0<=sr2<r and 0<=sc2<c):
                    sr2 -= dr2; sc2 -= dc2
                    dr2, dc2 = -dc2, dr2
                    sr2 += dr2; sc2 += dc2
                pr2, pc2 = sr2, sc2
            if works: break
    ans = min(ans, sum(m1[i]!=d1[i] for i in s), sum(m2[i]!=d2[i] for i in s))
    s = s[::-1]
print(ans)