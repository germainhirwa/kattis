from collections import deque

v, e, d = map(int, input().split())
g = {}
n2v = {}
skep = [0]*v
for i in range(v):
    name, t = input().split()
    n2v[name] = i
    skep[i] = int(t)
for _ in range(e):
    i, j = input().split()
    for _ in range(2):
        if n2v[i] not in g: g[n2v[i]] = []
        g[n2v[i]].append(n2v[j])
        i, j = j, i
s = n2v[input().strip()]
spread = [0]*v
q = deque([(s, 0)])
done = set()
while q:
    u, dd = q.popleft()
    if dd >= d: break
    if spread[u] < skep[u] or u in done: continue
    done.add(u)
    if u in g:
        for u2 in g[u]:
            spread[u2] += 1
            q.append((u2, dd+1))
print(sum(map(bool, spread[:s] + spread[s+1:])))