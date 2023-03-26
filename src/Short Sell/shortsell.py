n, k = map(int, input().split())
a, p = list(map(int, input().split())), []
for i in range(1, n): p.append(100*(a[i-1]-a[i])-k)
c = s = 0
for i in p: s, c = max(s+i, 0), max(c, s+i)
print(max(c-k, 0))