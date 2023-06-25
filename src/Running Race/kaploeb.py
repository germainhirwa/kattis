l, k, s = map(int, input().split())
d = {}
for _ in range(l):
    p, t = input().split()
    p, (h, m) = int(p), map(int, t.split('.'))
    if p not in d: d[p] = [0, 0]
    d[p][0] += 60*h+m
    d[p][1] += 1
f = []
for i, (t, l) in d.items():
    if l == k: f.append((t, i))
for _, i in sorted(f): print(i)