n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
t = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            t += s[i][j] + s[j][k] + s[k][i] == 3
print(t)