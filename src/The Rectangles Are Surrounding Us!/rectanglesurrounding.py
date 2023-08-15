import sys; input = sys.stdin.readline
while (n:=int(input())):
    g = [[0]*501 for _ in range(501)]
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        for x in range(a, c):
            for y in range(b, d): g[x][y] = 1
    print(sum(map(sum, g)))