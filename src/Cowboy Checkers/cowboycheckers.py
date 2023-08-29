s = [[*input().strip()] for _ in range(7)]
s[3][3] = 'X'
dm = {
    ((0,0), (0,3), (0,6)),
    ((1,1), (1,3), (1,5)),
    ((2,2), (2,3), (2,4)),
    ((3,0), (3,1), (3,2)),
    ((3,4), (3,5), (3,6))
}
dm = dm | set(((6-a, b), (6-c, d), (6-e, f)) for (a, b), (c, d), (e, f) in dm)
dm = dm | set(((b, a), (d, c), (f, e)) for (a, b), (c, d), (e, f) in dm)
ww = set()
for (a, b), (c, d), (e, f) in dm:
    if s[a][b] == s[c][d] == s[e][f] == 'W': ww.add(((a, b), (c, d), (e, f)))
if not ww: print('no double mill'), exit(0)
for i in range(7):
    for j in range(7):
        if s[i][j] == 'W':
            dd = 1
            while 0<=i+dd<7:
                if s[i+dd][j] in 'BWX-': break
                elif s[i+dd][j] != '|':
                    s[i+dd][j], s[i][j] = s[i][j], s[i+dd][j]
                    xx = set()
                    for (a, b), (c, d), (e, f) in dm:
                        if s[a][b] == s[c][d] == s[e][f] == 'W': xx.add(((a, b), (c, d), (e, f)))
                    if len(ww&xx) == len(ww)-1 == len(xx)-1: print('double mill'), exit(0)
                    s[i+dd][j], s[i][j] = s[i][j], s[i+dd][j]
                dd += 1
            dd = -1
            while 0<=i+dd<7:
                if s[i+dd][j] in 'BWX-': break
                elif s[i+dd][j] != '|':
                    s[i+dd][j], s[i][j] = s[i][j], s[i+dd][j]
                    xx = set()
                    for (a, b), (c, d), (e, f) in dm:
                        if s[a][b] == s[c][d] == s[e][f] == 'W': xx.add(((a, b), (c, d), (e, f)))
                    if len(ww&xx) == len(ww)-1 == len(xx)-1: print('double mill'), exit(0)
                    s[i+dd][j], s[i][j] = s[i][j], s[i+dd][j]
                dd -= 1
            dd = 1
            while 0<=j+dd<7:
                if s[i][j+dd] in 'BWX|': break
                elif s[i][j+dd] != '-':
                    s[i][j+dd], s[i][j] = s[i][j], s[i][j+dd]
                    xx = set()
                    for (a, b), (c, d), (e, f) in dm:
                        if s[a][b] == s[c][d] == s[e][f] == 'W': xx.add(((a, b), (c, d), (e, f)))
                    if len(ww&xx) == len(ww)-1 == len(xx)-1: print('double mill'), exit(0)
                    s[i][j+dd], s[i][j] = s[i][j], s[i][j+dd]
                dd += 1
            dd = -1
            while 0<=j+dd<7:
                if s[i][j+dd] in 'BWX|': break
                elif s[i][j+dd] != '-':
                    s[i][j+dd], s[i][j] = s[i][j], s[i][j+dd]
                    xx = set()
                    for (a, b), (c, d), (e, f) in dm:
                        if s[a][b] == s[c][d] == s[e][f] == 'W': xx.add(((a, b), (c, d), (e, f)))
                    if len(ww&xx) == len(ww)-1 == len(xx)-1: print('double mill'), exit(0)
                    s[i][j+dd], s[i][j] = s[i][j], s[i][j+dd]
                dd -= 1
print('no double mill')