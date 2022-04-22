import sys
from collections import deque

m = []
for line in sys.stdin:
    m.append(list(line.strip()))

r, c = len(m), len(m[0])
sr, sc = r - 1, 0
ices = {}
for i in range(r):
    for j in range(c):
        if m[i][j] == 'D':
            gr, gc = i, j
        elif m[i][j] == 'I':
            ices[(i, j)] = len(ices)

def valid(i, j):
    return 0 <= i < r and 0 <= j < c
dd = {
    'R': (0, 1), 'L': (0, -1),
    'U': (-1, 0), 'D': (1, 0)
}
lr = {
    'R': ('U', 'D'), 'L': ('D', 'U'),
    'U': ('L', 'R'), 'D': ('R', 'L')
}

solved = {(sr, sc, 'R')}
q = deque([(sr, sc, 'R', [0] * len(ices), '')])
while q:
    rr, cc, dir, ii, path = q.popleft()
    if m[rr][cc] == 'D':
        print(path)
        sys.exit(0)
    dr, dc = dd[dir]
    if valid(rr + dr, cc + dc) and (rr + dr, cc + dc, dir) not in solved:
        if m[rr + dr][cc + dc] == 'I':
            # Ice already destroyed, can proceed
            if ii[ices[(rr + dr, cc + dc)]]:
                q.append((rr + dr, cc + dc, dir, ii.copy(), path + 'F'))
                solved.add((rr + dr, cc + dc, dir))
            else:
                ii2 = ii.copy()
                ii2[ices[(rr + dr, cc + dc)]] = 1
                q.append((rr, cc, dir, ii2, path + 'X'))
                solved.add((rr, cc, dir))
        elif m[rr + dr][cc + dc] != 'C':
            q.append((rr + dr, cc + dc, dir, ii.copy(), path + 'F'))
            solved.add((rr + dr, cc + dc, dir))
    nl, nr = lr[dir]
    if (rr, cc, nl) not in solved:
        solved.add((rr, cc, nl))
        q.append((rr, cc, nl, ii.copy(), path + 'L'))
    if (rr, cc, nr) not in solved:
        solved.add((rr, cc, nr))
        q.append((rr, cc, nr, ii.copy(), path + 'R'))
print('no solution')