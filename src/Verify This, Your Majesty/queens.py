n = int(input())
ok = True

xx, yy, xpy, xmy = [False] * n, [False] * n, [False] * (2*n), [False] * (2*n)
for _ in range(n):
    x, y = list(map(int, input().split()))
    if xx[x] or yy[y] or xpy[x + y] or xmy[x - y + n]:
        ok = False
        break
    xx[x], yy[y], xpy[x + y], xmy[x - y + n] = [True] * 4

print(['INCORRECT', 'CORRECT'][int(ok)])