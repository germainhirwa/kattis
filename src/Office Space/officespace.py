import sys; input = sys.stdin.readline
while True:
    try: w, h = map(int, input().split())
    except: break
    g = [[0]*(h+1) for _ in range(w+1)]; m = {}
    for _ in range(int(input())):
        k, *r = input().split(); a, b, c, d = map(int, r); m[k] = 0
        for x in range(a, c):
            for y in range(b, d):
                if g[x][y] == 0: g[x][y] = k
                elif g[x][y] != 0: g[x][y] = '@'
    print('Total', w*h); u = c = 0
    for i in range(w+1):
        for j in range(h+1):
            if g[i][j] == 0: u += 1
            elif g[i][j] == '@': c += 1
            else: m[g[i][j]] += 1
    print('Unallocated', u-w-h-1), print('Contested', c)
    for i in m.items(): print(*i)
    print()