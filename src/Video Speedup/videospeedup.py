n, p, k = list(map(int, input().split()))
t = list(map(int, input().split()))
t.append(k)

ans = t[0]
for i in range(n):
    ans += (100 + p*(i+1))/100 * (t[i+1] - t[i])
print(ans)