import sys; input = sys.stdin.readline
for _ in range(int(input())):
    p, n = map(int, input().split())
    a = sorted(enumerate(map(int, input().split())), key=lambda x: (x[1], -x[0]))
    w = [0]*n
    for t, (i, c) in enumerate(a):
        x = min(c, p//(n-t))
        p -= x; w[i] = x
    if p: print('IMPOSSIBLE')
    else: print(*w)