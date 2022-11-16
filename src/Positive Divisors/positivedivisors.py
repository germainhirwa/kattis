s, b = [], []
n = int(input())
p = 1
while p*p <= n:
    if n % p == 0:
        s.append(p)
        if p*p != n:
            b.append(n//p)
    p += 1
for i in s:
    print(i)
for i in b[::-1]:
    print(i)