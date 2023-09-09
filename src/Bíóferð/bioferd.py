import sys; input = sys.stdin.readline
from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

n = int(input()); V = 2*n
g = [[*map(lambda x: int(x)+n-1, input().split()[1:])] for _ in range(n)]
for _ in range(n): g.append([])
for i in range(n):
    for j in g[i]: g[j].append(i)
match, mcbm = [-1]*V, 0
free = {*range(n)}
nfree = len(free)
for l in [*free]:
    if (candidates:=[r for r in g[l] if match[r] == -1]): mcbm += 1; free.discard(l); match[choice(candidates)] = l
for f in free: vis = [0]*nfree; mcbm += aug(f)

if mcbm != n: print('Neibb')
else: print(*(match[i]+1 for i in range(n, 2*n)))