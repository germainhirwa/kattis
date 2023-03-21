n, m = map(int, input().split())
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))

best = 1e9
for i in range(n):
    for j in range(m):
        cost = 0
        for ii in range(n):
            for jj in range(m):
                cost += (abs(i-ii) + abs(j-jj))*p[ii][jj]
        best = min(best, cost)
print(best)