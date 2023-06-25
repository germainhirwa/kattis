n, k = map(int, input().split())
p, t = [], set()
for i in range(n):
    a, d, h = map(int, input().split())
    p.append((a, d, h))
for i in range(3):
    for pp in sorted(p, key=lambda x: -x[i])[:k]: t.add(pp)
print(len(t))