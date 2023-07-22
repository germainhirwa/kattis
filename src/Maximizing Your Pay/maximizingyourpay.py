from itertools import combinations
import sys; input = sys.stdin.readline

INF = 1e18
def tsp(G):
    n = len(G); C = [[INF for _ in range(n)] for _ in range(1<<n)]; C[1][0] = 0
    for s in range(1, n):
        for S in combinations(range(1, n), s):
            k = 1
            for i in S: k += 1<<i
            for i in S:
                if i == 0: continue
                C[k][i] = min(C[k][i], C[k^(1<<i)][0]+G[0][i])
                for j in S:
                    if j != i: C[k][i] = min(C[k][i], C[k^(1<<i)][j]+G[j][i])
    r = -min(C[i][j]+G[0][j] for i in range(1, len(C), 2) for j in range(n))
    return r if r != -INF else 1

while True:
    l = input().split()
    if len(l) == 1: break
    V, E = map(int, l); G = [[INF]*V for _ in range(V)]
    for _ in range(E): a, b = map(int, input().split()); G[a][b] = G[b][a] = -1
    print(tsp(G))