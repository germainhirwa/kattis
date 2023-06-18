r, c = map(int, input().split())
q = [['.']*c for _ in range(r)]
p = []
for _ in range(int(input())):
    r2, c2 = map(int, input().split())
    m = [input().strip() for _ in range(r2)]
    p.append(m)
for _ in range(int(input())):
    qj, tj, pj = map(int, input().split())
    pp = p[pj-1]
    rp, cp = len(pp), len(pp[0])
    for i in range(rp):
        for j in range(cp):
            try:    q[qj+i][tj+j] = pp[i][j]
            except: pass
for s in q: print(''.join(s))