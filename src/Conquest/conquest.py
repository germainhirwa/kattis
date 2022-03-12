from heapq import *
import sys

v, e = map(int, input().split())
g, size = {}, []
q = [0]
vis = [False] * v

for line in sys.stdin:
    if e != 0:
        a, b = map(int, line.split())
        a -= 1
        b -= 1
        if a not in g:
            g[a] = []
        if b not in g:
            g[b] = []
        g[a].append(b)
        g[b].append(a)
        e -= 1
    else:
        size.append(int(line))

ans = size[0]
seen = set()
while q:
    h = heappop(q)
    if h in seen:
        continue
    s, i = h // v, h % v
    vis[i] = True
    seen.add(h)
    if s >= ans:
        break
    else:
        ans += s
        if i in g:
            for w in g[i]:
                if not vis[w]:
                    heappush(q, size[w] * v + w)
print(ans)