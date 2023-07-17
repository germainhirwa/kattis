N = int(input())
speak, uds = [], []
for i in range(N):
    _, s, *u = input().strip().split()
    speak.append(s), uds.append(set(u+[s]))
g, gt = [[] for _ in range(N)], [[] for _ in range(N)]
for a in range(N-1):
    for b in range(a+1, N):
        if speak[a] in uds[b]: g[a].append(b), gt[b].append(a)
        if speak[b] in uds[a]: g[b].append(a), gt[a].append(b)
top, vis, scc = [], set(), []
def DFS(s, add):
    vis.add(s)
    a = gt if add else g
    for v in a[s]:
        if v not in vis: DFS(v, add)
    if add: top.append(s)
    else: scc[-1] += 1
for i in range(N):
    if i not in vis: DFS(i, True)
vis.clear()
for i in top[::-1]:
    if i not in vis: scc.append(0); DFS(i, False)
print(N-max(scc))