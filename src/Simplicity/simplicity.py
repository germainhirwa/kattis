s, d = input(), {}
for c in s:
    d[c] = d.get(c, 0) + 1
d = sorted(list(d.items()), key=lambda x: -x[1])
print(sum(map(lambda x: x[1], d[2:])))