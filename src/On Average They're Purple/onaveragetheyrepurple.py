from collections import deque
v, e = map(int, input().split())
g = [[] for _ in range(v)]
for _ in range(e):
    a, b = map(int, input().split())
    a -= 1; b -= 1; g[a].append(b), g[b].append(a)
col, q = {}, deque([(0, 0)])
while q:
    u, d = q.popleft()
    for w in g[u]:
        if (min(u, w), max(u, w)) not in col:
            col[(min(u, w), max(u, w))] = d%2
            q.append((w, d+1))
q, ve, c = deque([(0, 1, 0)]), set(), 1e9
while q:
    u, cc, ch = q.popleft()
    for w in g[u]:
        tup = (min(u, w), max(u, w))
        if v-1 in tup: c = min(c, ch)
        if tup not in ve:
            ve.add(tup)
            q.append((w, col[tup], ch + (cc != col[tup])))
print(c)