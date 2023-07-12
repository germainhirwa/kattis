import sys
from collections import deque, defaultdict, Counter

mem = {}
def ps(n):
    if n in mem: return mem[n]
    s = ['']
    for i in str(n):
        s2 = []
        for j in s: s2.append(j), s2.append(j+i)
        s = s2
    mem[n] = {*map(int, s[1:])}; return mem[n]

mem2 = {}
def xsf(n):
    if n in mem2: return mem2[n]
    p, x, m = ps(n), [], str(n)
    for s in [str(i) for i in p if n>i>1 and n%i == 0]:
        # discard digits of s from m
        y, m2 = [], [*m]
        def bt(c, k):
            if not c:
                if m2: y.append(int(''.join(m2)))
                return
            for i in range(k, len(m2)):
                u = m2[i]
                if u == c[-1]: c.pop(), m2.pop(i), bt(c, i), m2.insert(i, u), c.append(u)
                bt(c, i+1)
        bt([*s[::-1]], 0), x.extend(y)
    mem2[n] = {*x}; return mem2[n]

def bt(g, s, cp):
    if len(cp) == pl: return p.append(cp + [s])
    cp.append(s)
    for t in g[s]: bt(g, t, cp)
    cp.pop()

q = deque()
for l in sys.stdin:
    n = int(l)
    if not n: break
    p = []
    q.append((n, 0)); g, D = {}, defaultdict(lambda: 1e9)
    while q:
        u, d = q.popleft()
        if D[u] < d: continue
        D[u] = d; g[u] = xsf(u)
        for v in g[u]: q.appendleft((v, d-1))
    pl = -min(D.values())
    bt(g, n, []), print(*min(p))