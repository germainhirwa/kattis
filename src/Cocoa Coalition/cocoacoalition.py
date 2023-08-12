n, m, a = map(int, input().split())
if a%n == 0 or a%m == 0: print(1), exit(0)
for i in range(1, int(a**0.5)+2):
    if a % i == 0 and ((i<=n and a//i<=m) or (i<=m and a//i<=n)): print(2), exit(0)
a = n*m-a
for i in range(1, int(a**0.5)+2):
    if a % i == 0 and ((i<=n and a//i<=m) or (i<=m and a//i<=n)): print(2), exit(0)
print(3)