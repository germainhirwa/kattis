n, a = int(input()), list(map(int, input().split()))
p, s = [0]*(n+1), [0]*(n+1)
for i in range(n): p[i+1], s[n-i-1] = p[i]/2 + a[i], s[n-i]/2 + a[n-i-1]
print(*(p[i+1]+s[i]-a[i] for i in range(n)))