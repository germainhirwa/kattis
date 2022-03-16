import sys
input()

def check(p, n):
    if n % p != 0 or p == 1 or p == n:
        return False
    c1, c2 = abs(p - n//p) + 1, p + n//p - 1
    return c1 > 0 and c2 > 0 and c1 % 2 == c2 % 2 == 0

for line in sys.stdin:
    n = int(line)
    p = 1
    while p * p <= 2 * n and not check(p, 2 * n):
        p += 1
    if check(p, 2 * n):
        a, b = (abs(p - 2 * n // p) + 1) // 2, (p + 2 * n // p - 1) // 2
        res = list(map(str, range(min(a, b), max(a, b) + 1)))
        print(n, '=', ' + '.join(res))
    else:
        print('IMPOSSIBLE')