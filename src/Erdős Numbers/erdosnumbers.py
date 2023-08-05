import sys; input = sys.stdin.readline
rev = {}; g = {}; db = {}
for l in sys.stdin:
    s, *r = l.strip().split()
    if s not in rev: rev[s] = len(rev); g[rev[s]] = []
    db[rev[s]] = s
    for rr in r:
        if rr not in rev: rev[rr] = len(rev)
        g[rev[s]].append(rev[rr])
        if rev[rr] not in g: g[rev[rr]] = []
        g[rev[rr]].append(rev[s])
from collections import deque
D = [10**9]*len(rev)
q = deque([(rev['PAUL_ERDOS'], 0)])
vis = [0]*len(rev)
while q:
    u, d = q.popleft()
    if vis[u]: continue
    vis[u], D[u] = 1, d
    if u not in g: continue
    for v in g[u]: q.append((v, d+1))
for i in db: print(db[i], (D[i] if D[i] != 10**9 else 'no-connection'))