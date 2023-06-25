r, c, n = map(int, input().split())
cn = [input().strip().split() for _ in range(r)]
B, R = 0, 0
checks = [[(i, j+k) for k in range(n)] for i in range(r) for j in range(c-n+1)] + \
    [[(j+k, i) for k in range(n)] for i in range(c) for j in range(r-n+1)] + \
    [[(i+k, j+k) for k in range(n)] for i in range(r-n+1) for j in range(c-n+1)] + \
    [[(i-k, j+k) for k in range(n)] for i in range(n-1, r) for j in range(c-n+1)]
for check in checks:
    b, rd = n, n
    for i, j in check:
        x = cn[i][j]
        if x == 'R': rd -= 1
        elif x == 'B': b -= 1
    if b and not rd: R = 1
    elif rd and not b: B = 1
assert B + R < 2
if B: print('BLUE WINS')
elif R: print('RED WINS')
else: print('NONE')