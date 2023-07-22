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
    nxt = min((C[k][i]+G[0][i], i) for i in range(n))[1]
    return C[-1][nxt]+G[0][nxt]

for _ in range(int(input())):
    x, y = map(int, input().split()); xs, ys = map(int, input().split())
    beepers = [[*map(int, input().split())] for _ in range(int(input()))]; beepers.append((xs, ys))
    G = [[INF]*len(beepers) for _ in range(len(beepers))]
    for i in range(len(beepers)-1):
        x1, y1 = beepers[i]
        if x1 > x or y1 > y: continue
        for j in range(i+1, len(beepers)):
            x2, y2 = beepers[j]
            if x2 > x or y2 > y: continue
            G[i][j] = G[j][i] = abs(x2-x1) + abs(y2-y1)
    print(tsp(G))