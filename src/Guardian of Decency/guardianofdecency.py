import sys; input = sys.stdin.readline
from random import choice
N = int(input())
S = []
for _ in range(N):
    h, s, m, sp = input().strip().split()
    S.append((int(h), s, m, sp))

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

V = 2*N
g = [[] for _ in range(2*N)]
for i in range(N-1):
    for j in range(i+1, N):
        if abs(S[i][0]-S[j][0]) <= 40 and S[i][1] != S[j][1] and S[i][2] == S[j][2] and S[i][3] != S[j][3]: g[i].append(j+N), g[j].append(i+N)
match, mcbm = [-1]*V, 0
free = set(range(N))
nfree = len(free)
for l in list(free):
    candidates = [r for r in g[l] if match[r] == -1]
    if candidates:
        mcbm += 1
        free.discard(l)
        match[choice(candidates)] = l
for f in free:
    vis = [0]*nfree
    mcbm += aug(f)
print(N-mcbm//2)