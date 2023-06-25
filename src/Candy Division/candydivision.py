n = int(input())
p = 1
s = set()
while p*p <= n:
    if n % p == 0: s.add(p), s.add(n//p)
    p += 1
print(*sorted(map(lambda x: x-1, s)))