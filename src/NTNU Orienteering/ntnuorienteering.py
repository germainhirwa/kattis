import sys
from collections import deque
from heapq import *
C = L = -1
input()

INF = float('inf')
def fw(D):
    v = len(D)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

for l in sys.stdin:
    if C == L == -1:
        C, L = int(l), int(input())
        E = C*(C-1)//2
        D, ll = [[INF]*C for _ in range(C)], []
        for i in range(C): D[i][i] = 0
    elif E != 0:
        u, v, w = map(int, l.split())
        D[u][v] = D[v][u] = w
        E -= 1
    else:
        i, s, e = map(int, l.split())
        ll.append((i, s, e))
        L -= 1
        if L == 0:
            D, G = fw(D), [[] for _ in ll]
            ll.sort(key=lambda x: x[1:])
            for i in range(len(ll)):
                c, s, e = ll[i]
                for j in range(i+1, len(ll)):
                    c2, s2, e2 = ll[j]
                    if e + D[c][c2] <= s2: G[i].append(j)
            dp = [1]*len(ll)
            for i in range(len(ll)):
                for j in G[i]: dp[j] = max(dp[j], dp[i]+1)
            print(max(dp))
            C = L = -1