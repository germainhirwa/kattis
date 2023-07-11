n, a = int(input()), list(map(int, input().split()))
s = sum(a)
s1 = p1 = 0
for i in range(n):
    s1 += a[i]
    if s1 >= s//3: p1 = i+1; break
s2 = p2 = 0
for i in range(p1, n):
    s2 += a[i]
    if s2 >= s//3: p2 = i+1; break
if s//3 == s1 == s2: print(p1, p2)
else: print(-1)