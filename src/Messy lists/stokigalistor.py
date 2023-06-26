n, a = int(input()), [*map(int, input().split())]
s = sorted(a)
print(sum(s[i] != a[i] for i in range(n)))