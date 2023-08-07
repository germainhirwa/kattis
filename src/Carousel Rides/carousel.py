import sys; input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    best = (0, 0, 0)
    for _ in range(n):
        a, b = map(int, input().split())
        if a > m: continue
        best = max(best, (a/b, a, b))
    if best[1] == best[2] == 0: print('No suitable tickets offered')
    else: print(f'Buy {best[1]} tickets for ${best[2]}')