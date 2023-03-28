n, *a = map(int, input().split())
c, r, s = [], [], []
for i in range(n+1):
    f = 0
    for j in range(n+1):
        f *= i
        f += a[j]
    c.append(f)
r.append(c[0])
while len(r) != n+1:
    for i in range(len(c)-1): s.append(c[i+1]-c[i])
    r.append(s[0])
    c, s = s, []
print(*r)