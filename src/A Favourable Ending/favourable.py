import sys
from collections import deque

input()
v = -1
for l in sys.stdin:
    if v == -1:
        v = int(l)
        g, x, r, dp = [[] for _ in range(v)], [], {}, [0]*v
    elif v != 0:
        v -= 1
        n, *o = l.split()
        n = int(n)
        r[n] = len(r)
        if o[-1] == 'favourably': x.append(n)
        elif o[-1] == 'catastrophically': pass
        else: g[r[n]] = list(map(int, o))
        if v == 0:
            x, v = [r[i] for i in x], len(g)
            for i in range(v): g[i] = [r[j] for j in g[i]]
            top, indeg, q = [], [0]*v, deque([])
            for u in range(v):
                for w in g[u]: indeg[w] += 1
            for u in range(v):
                if indeg[u] == 0: q.append(u)
            top, q2 = [], list(q)
            while q:
                u = q.popleft()
                top.append(u)
                for w in g[u]:
                    indeg[w] -= 1
                    if indeg[w] == 0: q.append(w)
            for i in x: dp[i] = 1
            for i in reversed(top):
                for j in g[i]: dp[i] += dp[j]
            r, v = 0, -1
            for i in q2: r += dp[i]
            print(r)