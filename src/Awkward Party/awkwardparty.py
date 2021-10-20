n = int(input())
x = list(map(int, input().split()))

d = {}

for i in range(n):
    if x[i] not in d:
        d[x[i]] = [i, -n]
    else:
        d[x[i]] = min([i, d[x[i]][0]], d[x[i]], key = lambda x: x[0] - x[1])

ans = 1e10
for i in d:
    if d[i][0] - d[i][1] < n:
        ans = min(ans, d[i][0] - d[i][1])

if ans == 1e10:
    print(n)
else:
    print(ans)