from random import choice
import sys; input = sys.stdin.readline
N, M = map(int, input().split())
I = [*map(int, input().split())]
W = [[*map(int, input().split())] for _ in range(N)]
F = [[*map(int, input().split())] for _ in range(M)]
for i in range(M): F[i][0] -= 1; F[i][1] -= 1

D = [[W[i][j]+I[j]*(i!=j) for j in range(N)] for i in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

V = 2*M
g = [[] for _ in range(V)]
match, mcbm = [-1]*V, 0
free = set(range(M))
nfree = len(free)

for i in range(M):
    for j in range(M):
        if i == j: continue
        if F[i][2] + W[F[i][0]][F[i][1]] + I[F[i][1]] + D[F[i][1]][F[j][0]] <= F[j][2]: g[i].append(j+M)

for l in list(free):
    candidates = [r for r in g[l] if match[r] == -1]
    if candidates:
        mcbm += 1
        free.discard(l)
        match[choice(candidates)] = l
for f in free:
    vis = [0]*nfree
    mcbm += aug(f)
print(M-mcbm)