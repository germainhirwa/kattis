import sys; input = sys.stdin.readline; ev = []; x = 0
n = int(input()); f = [[*map(int, input().split())] for _ in range(n)]
m = int(input()); g = [[*map(int, input().split())] for _ in range(m)]
for xi, yi in f: ev.append((x, 0, 0, 0, yi)); x = xi
ev.append((x, 0, 0, 0, yi)); x = 0
for xi, ai, bi, ci in g: ev.append((x, 1, ai, bi, ci)); x = xi
ev.sort(); ev.append((x, 1, ai, bi, ci)); it = []
cx = 0; ff = ev[0][2:]; gg = ev[1][2:]; ev = ev[2:]; ans = 0
for i in range(len(ev)):
    nx, et, a, b, c = ev[i]
    fa, fb, fc = ff; ga, gb, gc = gg; bds = [cx]
    if (D:=gb*gb-4*ga*(gc-fc)) >= 0:
        if ga == 0:
            if gb: sol1 = sol2 = -(gc-fc)/gb
            else: sol1 = sol2 = None
        else:
            sol1 = (-gb-D**0.5)/2/ga
            sol2 = (-gb+D**0.5)/2/ga
        if sol1 != None and sol2 != None:
            if cx <= sol1 <= nx: bds.append(sol1)
            if sol1 != sol2 and cx <= sol2 <= nx: bds.append(sol2)
    bds.append(nx), bds.sort()
    ans += sum(abs((qq**3-pp**3)*(fa-ga)/3 + (qq**2-pp**2)*(fb-gb)/2 + (qq-pp)*(fc-gc)) for pp, qq in zip(bds, bds[1:]))
    if et == 0: ff = (a, b, c)
    else: gg = (a, b, c)
    cx = nx
print(ans)
