r, c = map(int, input().split())
m = [list(input().strip()) for _ in range(r)]
cf, delta = set(), ((-1, 0), (0, 1), (1, 0), (0, -1))
for i in range(r):
    for j in range(c):
        if m[i][j] == '#': continue
        has_c = 0
        for dr, dc in delta:
            if 0<=i+dr<r and 0<=j+dc<c and m[i+dr][j+dc] == 'E': has_c = 1
        if not has_c: m[i][j] = 'E'
for i in m: print(''.join(i))