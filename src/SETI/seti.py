def powmod(a, b, m):
    if b == 0:
        return 1
    elif b == 1:
        return a % m
    elif b % 2:
        return a * powmod(a * a % m, b // 2, m) % m
    return powmod(a * a % m, b // 2, m)

def inv(a, m): # m is prime
    return powmod(a, m - 2, m)

def solve(a, b, mod):
    for i in range(len(a)):
        a[i].append(b[i])
        for j in range(len(a[0])):
            a[i][j] %= mod
    col, row = 0, 0
    while col < len(a[0]) and row < len(a):
        sel = row
        for i in range(row, len(a)):
            if a[i][col] > a[sel][col]:
                sel = i
        for i in range(col, len(a[0])):
            a[sel][i], a[row][i] = a[row][i], a[sel][i]
        c_inv = inv(a[row][col], mod)
        for i in range(len(a)):
            if i != row:
                if a[i][col] == 0:
                    continue
                c = (a[i][col] * c_inv) % mod
                for j in range(len(a[0])):
                    a[i][j] -= c * a[row][j]
                    a[i][j] %= mod
        row += 1
        col += 1
    for i in range(len(a)):
        k = inv(a[i][i], mod)
        for j in range(len(a[0])):
            a[i][j] *= k
            a[i][j] %= mod
    return [x[-1] for x in a]

n = int(input())
for _ in range(n):
    p, s = input().split()
    p = int(p)
    s = list(map(lambda x: 0 if x == '*' else ord(x) - ord('a') + 1, s))
    a = [[(i + 1)**j for j in range(len(s))] for i in range(len(s))]
    print(*solve(a, s, p))