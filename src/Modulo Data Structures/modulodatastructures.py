from math import ceil
import sys; input = sys.stdin.readline
N, Q = map(int, input().split())
S = ceil(N**0.5)
A = [0]*(N+1)
B = [[0]*(S+1) for _ in range(S+1)]
for _ in range(Q):
    q, *n = map(int, input().split())
    if q == 1:
        a, b, c = n
        if b <= S: B[b][a] += c
        else:
            for j in range(a, N+1, b): A[j] += c
    else: print(A[n[0]] + sum(B[i][n[0]%i] for i in range(1, S+1)))