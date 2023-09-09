import sys; input = sys.stdin.readline
from collections import Counter
u, k = map(int, input().split())
f = []; rf = {}; r = []; rr = {}; l = []
for _ in range(u):
    r.append(input().strip()); rr[r[-1]] = len(rr)
    t = {}
    for _ in range(int(input())):
        ff, kk = input().split()
        if ff not in rf: f.append(ff); rf[ff] = len(rf)
        t[rf[ff]] = int(kk)
    l.append(t)
c = Counter(); d = Counter()
for _ in range(k):
    for _ in range(int(input())): b, kk = input().split(); d[b] += int(kk)
for b, a in d.items():
    for idx, v in l[rr[b]].items(): c[idx] += v*a
fin = []
for k, v in c.items():
    if v: fin.append((f[k], v))
for i in sorted(fin): print(*i)