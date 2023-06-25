n = int(input())
m = {}
a, b, c = set(), set(), set()
for _ in range(int(input())):
    c1, c2, p1, p2 = input().strip().split()
    c1, c2 = map(int, (c1, c2))
    if p1 != p2:
        if p1 not in m: m[p1] = set()
        if p2 not in m: m[p2] = set()
        m[p1].add(c1), m[p2].add(c2)
    else:
        a.add(c1), a.add(c2)
for i in m:
    for j in m[i]:
        if j not in a: [c, b][len(m[i]) == 2].add(j)
a, b, c = map(len, (a, b, c))
d, f = n-a-b-c, b//2
if c == d: f += c; c = d = 0
print(f + (d==2))