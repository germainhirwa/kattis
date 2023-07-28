import sys; input = sys.stdin.readline
from random import choice

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

for _ in range(int(input())):
    input(); R, C = map(int, input().split()); M = [[None]*C for _ in range(R)]; M2 = []
    for _ in range(int(input())): py, px = map(int, input().split()); M[py-1][px-1] = 1
    for _ in range(int(input())): wy, wx = map(int, input().split()); M[wy-1][wx-1] = 0
    for i in range(R):
        M2.append([None]*C)
        for j in range(C):
            if M[i][j] == 1: M2[-1][j] = 1
            elif M[i][j] == 0: M2.append([None]*C); M2[-1][j] = 0; M2.append([None]*C)
    R2 = len(M2); T = []; curr_row = -1; T = set()
    for i in range(C):
        curr_row += 1
        for j in range(R2):
            if M2[j][i] == 1: T.add((j, curr_row))
            elif M2[j][i] == 0: curr_row += 2
    R, C = R2, curr_row+1; V = R+C; g = [[] for _ in range(V)]
    for i, j in T: g[i].append(R+j)
    match, mcbm = [-1]*V, 0; free = set(range(R)); nfree = R
    for l in list(free):
        if (candidates:=[r for r in g[l] if match[r] == -1]): mcbm += 1; free.discard(l); match[choice(candidates)] = l
    for f in free: vis = [0]*nfree; mcbm += aug(f)
    print(mcbm)