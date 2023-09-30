n, m = list(map(int, input().split()))
p = list(map(int, input().split()))
s = 0
for i in range(m):
    if s + p[i] <= n:
        s += p[i]
    else:
        break
print(m - i)