from math import *

r, c, e = map(int, input().split())
m = []
for _ in range(r):
    m.append(['.'] * c)

charges = {}
for _ in range(e):
    rr, cc, s = input().split()
    rr, cc = int(rr) - 1, int(cc) - 1
    charges[(cc, rr)] = s

for i in range(r):
    for j in range(c):
        if (i, j) in charges:
            m[i][j] = charges[(i, j)]
        else:
            v = 0
            for ch in charges:
                rch, cch = ch
                dir = charges[ch]
                v += (2*int(dir == '+') - 1) / hypot(i - rch, j - cch)
            if v < 0:
                choose = '%Xx'
            else:
                choose = '0Oo'
            if abs(v) >= 1/pi:
                m[i][j] = choose[0]
            elif abs(v) >= 1/pi**2:
                m[i][j] = choose[1]
            elif abs(v) >= 1/pi**3:
                m[i][j] = choose[2]
for row in m:
    print(''.join(row))