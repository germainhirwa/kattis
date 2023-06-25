import sys

d, f = {}, {}
for _ in range(int(input())):
    k, _, *w = input().strip().split()
    f[k] = 0
    for i in w:
        if i not in d: d[i] = []
        d[i].append(k)
for l in sys.stdin:
    for i in l.strip().split():
        if i in d:
            for j in d[i]: f[j] += 1
m = max(f.values())
s = [i for i in f if f[i] == m]
for i in sorted(s): print(i)