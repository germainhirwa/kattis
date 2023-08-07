n = int(input())
m = [input() for _ in range(n)]
best = 0
for i in range(n):
    for j in range(n):
        if m[i][j] == 'S':
            d = 1e9
            for k in range(n):
                for l in range(n):
                    if m[k][l] == 'H': d = min(d, abs(i-k)+abs(j-l))
            best = max(best, d)
print(best)