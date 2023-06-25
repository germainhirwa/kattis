m = [list(input().strip()) for _ in range(8)]
r, c, dr, dc = 7, 0, 0, 1
d = input().strip()

try:
    for i in d:
        if i == 'F': r += dr; c += dc; assert m[r][c] in 'D.'
        if i == 'R': dr, dc = dc, -dr
        if i == 'L': dr, dc = -dc, dr
        if i == 'X':
            assert m[r+dr][c+dc] == 'I'
            m[r+dr][c+dc] = '.'
    assert m[r][c] == 'D'
    print('Diamond!')
except: print('Bug!')