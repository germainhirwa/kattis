import sys; input = sys.stdin.readline
for _ in range(int(input())):
    c, r = map(int, input().split())
    m = [[*map(int, input().split())] for _ in range(r)]
    rr, cc = [], []
    # minimzed if r, c = median(r), median(c)
    for i in range(r): rr.append((i, sum(m[i])))
    for i in range(c): cc.append((i, sum(m[j][i] for j in range(r))))
    t = sum(map(sum, m))//2
    tr = tc = 0
    for i in range(r):
        if tr + rr[i][1] >= t: mr = i; break
        tr += rr[i][1]
    for i in range(c):
        if tc + cc[i][1] >= t: mc = i; break
        tc += cc[i][1]
    print(sum(m[i][j]*(abs(mr-i)+abs(mc-j)) for i in range(r) for j in range(c)), 'blocks')