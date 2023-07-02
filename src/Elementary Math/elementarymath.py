from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

n = int(input())
h, e, r, r2 = {}, {}, [], []
for i in range(n):
    a, b = map(int, input().split())
    e[(a, b, len(e))] = len(e); r2.append((a, b))
    for j in [a-b, a+b, a*b]:
        if j not in h: h[j] = len(h)+n; r.append(j)

V = n+len(h)
g = [[] for _ in range(V)]
for a, b, t in e:
    for j in [a-b, a+b, a*b]: g[e[(a, b, t)]].append(h[j])
match, mcbm = [-1]*V, 0
free = set(range(n))
nfree = len(free)

for l in list(free):
    candidates = [r for r in g[l] if match[r] == -1]
    if candidates:
        mcbm += 1
        free.discard(l)
        match[choice(candidates)] = l

for f in free:
    vis = [0] * nfree
    mcbm += aug(f)

fin = [None]*n
if mcbm == n:
    for idx in range(n, V):
        if match[idx] != -1: fin[match[idx]] = r[idx-n]
    for i in range(n):
        a, b = r2[i]
        if a + b == fin[i]: print(f'{a} + {b} = {fin[i]}')
        elif a - b == fin[i]: print(f'{a} - {b} = {fin[i]}')
        else: print(f'{a} * {b} = {fin[i]}')
else: print('impossible')