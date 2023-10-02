n, b = map(int, input().split()); b += 1; f = 1; a = 0
while f <= n: f *= b; a += 1
print(a)