import sys
from collections import deque
from heapq import *

e = -1
for l in sys.stdin:
    if e == -1:
        try:
            v, e = map(int, l.split())
            g = [[] for _ in range(v)]
        except: continue
    else:
        a, b, w = map(int, l.split())
        g[a-1].append((b-1, w)), g[b-1].append((a-1, w))
        e -= 1
        if e == 0:
            D, e, dag, s = [3e9]*v, -1, [[] for _ in range(v)], 1
            D[s], pq = 0, [(0, s)]
            while pq:
                dd, vv = heappop(pq)
                if dd == D[vv]:
                    for nn, ww in g[vv]:
                        if D[nn] > dd + ww:
                            D[nn] = dd + ww
                            heappush(pq, (D[nn], nn))
            for i in range(v):
                for j, _ in g[i]:
                    if D[i] > D[j]: dag[i].append(j)
            indeg, q, g, top = [0]*v, deque(), dag, []
            for i in range(v):
                for j in g[i]: indeg[j] += 1
            for i in range(v):
                if not indeg[i]: q.append(i)
            while q:
                u = q.popleft()
                top.append(u)
                for w in g[u]:
                    indeg[w] -= 1
                    if indeg[w] == 0: q.append(w)
            dp = [0]*v
            dp[1] = 1
            for i in top[::-1]:
                for j in g[i]: dp[i] += dp[j]
            print(dp[0])