n, e = map(int, input().split())
ans = 0
for i in range(n + 1):
    if str(i).find(str(2**e)) != -1:
        ans += 1
print(ans)