n, s, t = int(input()), input(), input()
a = sum(s[i-1] != s[i] for i in range(n))
b = sum(t[i-1] != t[i] for i in range(n))
print(['no', 'yes'][a>b or(0<a==b<n)])