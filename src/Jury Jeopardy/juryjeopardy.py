n = int(input())
print(n)
for _ in range(n):
    move = input().strip()
    D = {(0, 0)}
    r, c, dr, dc = 0, 0, 0, 1
    for i in move:
        if i == 'L': dr, dc = -dc, dr
        elif i == 'R': dr, dc = dc, -dr
        elif i == 'B': dr, dc = -dr, -dc
        r += dr; c += dc
        D.add((r, c))
    minr, maxr, _, maxc = [f(map(lambda x: x[i], D)) for i in range(2) for f in [min, max]]
    R, C  = maxr-minr+3, maxc+2
    m = [['#']*C for _ in range(R)]
    print(R, C)
    for r, c in D: m[r-minr+1][c] = '.'
    for l in m: print(''.join(l))