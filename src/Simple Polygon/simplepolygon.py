import sys; input = sys.stdin.readline

for _ in range(int(input())):
    p = [*map(int, input().split())][1:]; n = len(p)//2; p = sorted((p[2*i], p[2*i+1], i) for i in range(n))
    (x1, y1, _), (x2, y2, _) = p[0], p[-1]
    a, b, c = y1-y2, x2-x1, x1*(y2-y1)-y1*(x2-x1)
    u = []; d = []; l = []
    for x, y, i in p[1:-1]:
        v = a*x+b*y+c
        if v > 0: u.append(i)
        elif v < 0: d.append(i)
        else: l.append(i)
    if u: print(p[0][2], *u, p[-1][2], *(d[::-1]+l[::-1]))
    else: print(p[0][2], *l, p[-1][2], *d[::-1])