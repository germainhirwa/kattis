n, m = map(int, input().split())
a = [int(input())-1 for _ in range(m)]
b = [1]*n
for i in a: b[i] = 0
c = [i for i in range(n) if b[i]]
r = []
a, c = a[::-1], c[::-1]
while a and c:
    if a[-1] < c[-1]:   r.append(a.pop())
    else:               r.append(c.pop())
r.extend(a[::-1])
r.extend(c[::-1])
for i in r: print(i+1)