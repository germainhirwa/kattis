n = int(input())
m = [[*map(int, input().split())] for _ in range(n)]
best = (0, 1e9, 1e9, 1e9)
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            best = min(best, (-m[i][j]*m[j][k]*m[k][i], i, j, k))
print(*(i+1 for i in best[1:]))