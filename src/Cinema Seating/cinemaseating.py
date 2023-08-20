import sys; input = sys.stdin.readline
R, C = map(int, input().split())
h = [[0]*C for _ in range(R)]; ans = [0]*9
for _ in range(int(input())): r, c = map(int, input().split()); h[r-1][c-1] = 1
for i in range(R):
    for j in range(C):
        if not h[i][j]: continue
        adj = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if (di or dj) and (0<=i+di<R and 0<=j+dj<C): adj += h[i+di][j+dj]
        ans[adj] += 1
print(*ans)