import sys; input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    d = sorted([int(input()) for _ in range(n)], reverse=True)
    k = sorted([int(input()) for _ in range(m)], reverse=True)
    s = 0
    while d and k:
        if d[-1] > k[-1]: k.pop(); continue
        d.pop(); s += k.pop()
    if d: print('Loowater is doomed!')
    else: print(s)