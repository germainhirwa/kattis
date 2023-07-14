import sys; input = sys.stdin.readline
n, p = int(input()), list(map(int, input().split()))
q = int(input())
g, s = [[] for _ in range(n)], []
for i in range(n): g[p[i]-1].append(i) if p[i] else s.append(i)
ti, to = [0]*n, [0]*n
t, vis = [0], [0]*n

def dfs(v):
    if vis[v]: return
    t[0] += 1; ti[v] = t[0]; vis[v] = 1
    for i in g[v]: dfs(i)
    t[0] += 1; to[v] = t[0]

def merge(intervals):
    h=lambda a,b:0 if a[1]<b[0]or b[1]<a[0]else(min(a[0],b[0]),max(a[1],b[1]))
    return [r:=[],[[r.pop(),r.append(k)]if r and(k:=h(r[-1],j))else r.append(j)for j in sorted(intervals)]][0]

for i in s: dfs(i)
for _ in range(q): print(sum((o-i+1)//2 for i,o in merge([(ti[i-1], to[i-1]) for i in list(map(int, input().split()))[1:]])))