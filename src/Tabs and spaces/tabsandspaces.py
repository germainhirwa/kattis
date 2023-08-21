f = [[int(input()) for _ in range(int(input()))] for _ in range(int(input()))]
best = (-1, -100)
for tab in range(1, 80):
    ans = 0
    for ff in f:
        for l in ff: t, s = l//tab, l%tab; ans += l-t-s
    best = max(best, (ans, -tab))
print(-best[1]), print(best[0])